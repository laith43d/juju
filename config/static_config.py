import os

# PATHS----------------------------------------------------

BASE_DIR = os.getcwd()
API_PREFIX = ''
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 'O' for Orator, 'SA' for SQLAlchemy
ORM = 'O'


class Config():
    # STATIC CONFIG--------------------------------------------

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
	'mysql': 'mysql',
        'postgres': 'postgres',
	'sqlite': 'sqlite'
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
	    'driver': DB_DIALECT,
	    'host': DB_HOST,
            'database': DB_NAME,
	    'user': DB_USERNAME,
            'password': DB_PASSWORD,
	    'prefix': DB_PREFIX
        }
    }


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
