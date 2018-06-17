import logging
import os
from logging.handlers import RotatingFileHandler
import redbeat
from celery.schedules import crontab

# PATHS----------------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
API_PREFIX = ''

REDIS_HOST = '127.0.0.1'

# Logging -------------------------------------------------

formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(
    'logs/app.log', maxBytes=1000000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
LOG_LEVEL = logging.DEBUG




class Config():
    # STATIC CONFIG--------------------------------------------

    REDIS_DOMAIN = 'redis://{}:6379'.format(REDIS_HOST)
    AUTH_REDIS_URL = 'redis://{}:6379/0'.format(REDIS_HOST)


    CELERY_BROKER_URL = '{}/{}'.format(REDIS_DOMAIN, 1)

    CELERY_RESULT_BACKEND = '{}/{}'.format(REDIS_DOMAIN, 1)

    CELERY_WORKER_CONFIG = {
        'broker': CELERY_BROKER_URL,
        'loglevel': LOG_LEVEL,
        'traceback': True,
        'worker_max_tasks_per_child': 50
    }


    REDBEAT_REDIS_URL = '{}/{}'.format(REDIS_DOMAIN, 3)
    REDBEAT_KEY_PREFIX = 'redbeat'
    REDBEAT_LOCK_KEY = 'redbeat:lock'
    # REDBEAT_LOCK_TIMEOUT = 2

    CELERY_BEAT_CONFIG = {
        'broker': CELERY_BROKER_URL,
        'loglevel': LOG_LEVEL,
        'traceback': True,
        'scheduler_cls': redbeat.RedBeatScheduler,
    }

    CELERY_DEFAULT_QUEUE = 'default'

    CELERYBEAT_SCHEDULE = {
        'task_1': {
            'task'    : 'task_1',
            'schedule': crontab(minute = "*/1")
        }
    }

    CELERY_QUEUES = {
        'default': {
            "exchange": "default",
            "binding_key": "default",
        },
        'queue1': {
            'exchange': 'queue1',
            'routing_key': 'queue1',
        },
        'queue2': {
            'exchange': 'queue2',
            'routing_key': 'queue2',
        },
        'queue3': {
            'exchange': 'queue3',
            'routing_key': 'queue3',
        },
        'queue4': {
            'exchange': 'queue4',
            'routing_key': 'queue4',
        },
        'queue5': {
            'exchange': 'queue5',
            'routing_key': 'queue5',
        }
    }

    # CELERY_ROUTES = {}

    CELERYD_TASK_SOFT_TIME_LIMIT = 120

    SOCKETIO_MESSAGE_QUEUE = 'redis://'

    CACHE_CONFIG = {
        'CACHE_TYPE'      : 'redis',
        'CACHE_KEY_PREFIX': 'fcache_',
        'CACHE_REDIS_HOST': 'localhost',
        'CACHE_REDIS_PORT': '6379',
        'CACHE_REDIS_URL' : '{}/{}'.format(REDIS_DOMAIN, 2)
    }

    IS_AUTH_ENABLED = True
    IS_ERROR_MAIL_ENABLED = False


    ADMINS = ['admin@webmaster.com']

    DEBUG = False
    TESTING = False

    HOST = '127.0.0.1'
    PORT = 8000

    # use your own secret keys---------------------------------
    # each key should be unique--------------------------------

    SECRET_KEY = 'f4f6b032d87bf6915832ed19e1b5823717b7fbd83a3e24513a25b34a859173786aab50e0921ab855c5f90725f852e53136f71e111aaaf1cfd0a99d797a539af9cb43f66d65417944ad4dc5fa04e9abcb3282138fddc578fb8a68c4232324c3eb4c681c42630a15dae3e680027aff11d552844c71316e340bee6684d1ea5e510f'
    JWT_SECRET_KEY = 'f4f6b032d87bf6915832ed19e1b5823717b7fbd83a3e24513a25b34a859173786aab50e0921ab855c5f90725f852e53136f71e111aaaf1cfd0a99d797a539af9cb43f66d65417944ad4dc5fa04e9abcb3282138fddc578fb8a68c4232324c3eb4c681c42630a15dae3e680027aff11d552844c71316e340bee6684d1ea5e510f'

    # DB STATIC CONFIG-----------------------------------------

    DB_DIALECTS = {
        'mysql'   : 'mysql',
        'postgres': 'postgres',
        'sqlite'  : 'sqlite'
    }

    DB_DIALECT = DB_DIALECTS['mysql']
    DB_NAME = 'juju'
    DB_HOST = 'localhost'
    DB_READ_HOST_NAME = 'localhost'
    DB_WRITE_HOST_NAME = 'localhost'
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_PREFIX = ''
    DB_QUERY_LOGGING = False

    # DB CONFIG------------------------------------------------

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if DB_DIALECT == 'sqlite':
        SQLALCHEMY_DATABASE_URI = f'{DB_DIALECT}:///{DB_NAME}.db'
    else:
        SQLALCHEMY_DATABASE_URI = f'{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    ORATOR_DATABASES = {
        DB_DIALECT: {
            'driver'  : DB_DIALECT,
            'host'    : DB_HOST,
            'database': DB_NAME,
            'user'    : DB_USERNAME,
            'password': DB_PASSWORD,
            'prefix'  : DB_PREFIX
        }
    }


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}

current_config = config['development']