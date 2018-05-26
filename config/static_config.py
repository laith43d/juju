import os

# STATIC CONFIG--------------------------------------------

NAME = 'JUJU 0.1'

# set this to false in a non-development environment-------
# CAUTION: very dangerous----------------------------------

DEBUG = True

HOST = '127.0.0.1'
PORT = 8000

# use your own secret keys---------------------------------
# each key should be unique--------------------------------

SECRET_KEY = 'f4f6b032d87bf6915832ed19e1b5823717b7fbd83a3e24513a25b34a859173786aab50e0921ab855c5f90725f852e53136f71e111aaaf1cfd0a99d797a539af9cb43f66d65417944ad4dc5fa04e9abcb3282138fddc578fb8a68c4232324c3eb4c681c42630a15dae3e680027aff11d552844c71316e340bee6684d1ea5e510f'
JWT_SECRET_KEY = 'f4f6b032d87bf6915832ed19e1b5823717b7fbd83a3e24513a25b34a859173786aab50e0921ab855c5f90725f852e53136f71e111aaaf1cfd0a99d797a539af9cb43f66d65417944ad4dc5fa04e9abcb3282138fddc578fb8a68c4232324c3eb4c681c42630a15dae3e680027aff11d552844c71316e340bee6684d1ea5e510f'

# PATHS----------------------------------------------------

BASE_DIR = os.getcwd()
API_PREFIX = ''
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# DB STATIC CONFIG-----------------------------------------

DB_DIALECTS = {
    'mysql'     : 'mysql',
    'postgres': 'postgres',
    'sqlite'    : 'sqlite'
}
DB_DRIVERS = {
    'mysql'     : 'mysqlclient',
    'postgres': 'psycopg2'
}

DB_DIALECT = DB_DIALECTS['mysql']
DB_DRIVER = DB_DRIVERS['mysql']
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

sql_config = {
    'SQL_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
    'SQL_ISOLATION_LEVEL': 'SERIALIZABLE',
    'SQL_ECHO': True,
    'SQL_ECHO_POOL': False,
    'SQL_CONVERT_UNICODE': True,
    'SQL_POOL_SIZE': 5,
    'SQL_POOL_TIMEOUT': 30,
    'SQL_POOL_RECYCLE': 3600,
    'SQL_MAX_OVERFLOW': 10,
    'SQL_AUTOCOMMIT': False,
    'SQL_AUTOFLUSH': True,
    'SQL_EXPIRE_ON_COMMIT': True
}

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

PONY = {
    'provider': DB_DRIVER,
    'user'    : DB_USERNAME,
    'password': DB_PASSWORD,
    'dbname'  : DB_NAME
}
