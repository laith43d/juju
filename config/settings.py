import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_orator import Orator
from flask_pony import Pony
from flask_praetorian import Praetorian
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mixins import AllFeaturesMixin

from config.static_config import LOG_DIR, ORM

# APP Initialization --------------------------------------

app = Flask(__name__)
app.config.from_object('config.static_config')

# Modules Initialization ----------------------------------

CORS(app)
limit = Limiter(
    app,
    key_func = get_remote_address,
    default_limits = ["200 per day", "50 per hour"]
)

# DB Init -------------------------------------------------

# If you use Pony ORM, uncomment this section -------------
if ORM == 'PONY':
    db = Pony(app).db
    Model = db.Entity

# If you use Orator ORM, uncomment this section -----------
if ORM == 'ORATOR':
    db = Orator(app)
    Model = db.Model

if ORM == 'SQLALCHEMY':
    # If you use SQLAlchemy, uncomment this section -------
    db = SQLAlchemy(app)
    Base = db.Model


    # we use AllFeaturesMixin to Inject all Mixins --------
    class Model(Base, AllFeaturesMixin):
        __abstract__ = True
        pass

    # set DB session --------------------------------------
    session = db.session

    # -----------------------------------------------------
    # setup base model: inject session so
    # it can be accessed from model
    # -----------------------------------------------------
    Model.set_session(session)

# Jwt -----------------------------------------------------
# for usage check out the user example --------------------
# https://github.com/laith43d/JUJU-User-Example -----------

app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

from db.models import User

guard = Praetorian(app = app, user_class = User)

# Logging -------------------------------------------------

formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(LOG_DIR + '/app.log', maxBytes = 1000000, backupCount = 5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# logger shortcut, example: Log.info('your message'),
# that would automatically be logged in the log file
# specified above.
Log = app.logger

# Registered Api & Models ---------------------------------
from api import *
from db.models import *