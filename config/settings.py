from logging.handlers import RotatingFileHandler
import logging

from dash import Dash
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_marshmallow import Marshmallow
from flask_praetorian import Praetorian
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mixins import AllFeaturesMixin

from config.static_config import LOG_DIR

# APP Initialization --------------------------------------

app = Flask(__name__)
app.config.from_object('config.static_config')

# Modules Initialization ----------------------------------

bcrypt = Bcrypt(app)
CORS(app)
ma = Marshmallow(app)
limit = Limiter(
	app,
	key_func = get_remote_address,
	default_limits = ["200 per day", "50 per hour"]
)

# DB Init -------------------------------------------------

db = SQLAlchemy(app)


class BaseModel(db.Model, AllFeaturesMixin):
	pass

# Jwt -----------------------------------------------------


app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

guard = Praetorian()
# The User class argument supplied during initialization
# represents the class that should be used to check for
# authorization for decorated routes.
# The class itself may be implemented in any way that you see fit.
# It must, however, satisfy the following requirements:
#
# Provide a lookup class method that:
#   should take a single argument of the name of the user
#   should return an instance of the user_class or None
# Provide an identify class method
#   should take a single argument of the unique id of the user
#   should return an instance of the user_class or None
# Provide a rolenames instance attribute
#   should return a list of string roles assigned to the user
# Provide a password instance attribute
#   should return the hashed password assigned to the user
# Provide an identity instance attribute
#   should return the unique id of the user

# Uncomment the following line after creating and importing the `User` class

from models import User
guard.init_app(app, User)

# Logging -------------------------------------------------

formatter = logging.Formatter(
	"[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(LOG_DIR + '/app.log', maxBytes = 1000000, backupCount = 5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# logger shortcut, example: Log.info('your message'), that would automatically be logged in the log file
# specified above.
Log = app.logger

# Registered Api & Models ---------------------------------

from api import *
from models import *