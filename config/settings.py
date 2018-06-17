import redis
from celery import Celery
from flask import Flask
from flask_cache import Cache
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mail import Mail
from flask_praetorian import Praetorian
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mixins import AllFeaturesMixin
from config.static_config import handler, current_config

# APP Initialization --------------------------------------

socketio = SocketIO()
cache = Cache()
mail = Mail()
db = SQLAlchemy()
guard = Praetorian()
limit = Limiter(
    key_func = get_remote_address,
    default_limits = ["200 per day", "50 per hour"])


celery_app = Celery(__name__,
                    broker = current_config.CELERY_BROKER_URL,
                    backend = current_config.CELERY_RESULT_BACKEND)
celery_app.autodiscover_tasks([__name__])

redis_client = redis.StrictRedis.from_url(current_config.REDIS_DOMAIN, db = 0)
auth_redis_client = redis.StrictRedis.from_url(current_config.AUTH_REDIS_URL)

# Import Socket.IO events so that they are registered with Flask-SocketIO
from . import events


# we use AllFeaturesMixin to Inject all Mixins ------------
class Model(db.Model, AllFeaturesMixin):
    __abstract__ = True
    pass

# ---------------------------------------------------------
# setup base model: inject session so
# it can be accessed from model
# ---------------------------------------------------------
Model.set_session(db.session)

def create_app(main = True):

    app = Flask(__name__)
    app.config.from_object(current_config)
    CORS(app, supports_credentials = True)
    db.init_app(app)
    limit.init_app(app)
    socketio.init_app(app)
    cache.init_app(app, config = current_config.CACHE_CONFIG)
    mail.init_app(app)

    # Jwt -----------------------------------------------------
    # for usage check out the user example --------------------
    # https://github.com/laith43d/JUJU-User-Example -----------

    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}

    from models import User
    guard.init_app(app=app, user_class=User)

    # Logging -------------------------------------------------

    app.logger.addHandler(handler)

    # logger shortcut, example: Log.info('your message'),
    # that would automatically be logged in the log file
    # specified above.
    Log = app.logger

    return app

# Registered Api & Models ---------------------------------

from api import *
from models import *
