from logging.handlers import RotatingFileHandler

from flask import Flask, logging
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_marshmallow import Marshmallow
from flask_orator import Orator
from config.static_config import LOG_DIR

# APP INITIALIZATION --------------------------------------

app = Flask(__name__)
app.config.from_object('config.static_config')

# MODULES INITIALIZATION ----------------------------------

bcrypt = Bcrypt(app)
CORS(app)
ma = Marshmallow(app)
limit = Limiter(
    app,
    key_func = get_remote_address,
    default_limits = ["200 per day", "50 per hour"]
)
jwt = JWTManager(app)

formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(LOG_DIR + '/app.log', maxBytes=1000000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# logger shortcut, example: Log.info('your message'), that would automatically be logged in the log file
# specified above.
Log = app.logger

# DB INIT -------------------------------------------------

db = Orator(app)

# REGISTERED Api-------------------------------------------

from api import *

