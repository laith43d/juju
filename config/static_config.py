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

SECRET_KEY = '4K5UA6+BMeyNPgYxhjFU03dYA1NlDGrf3wRr8uOcIHU='
JWT_SECRET_KEY = '4K5UA6+BMeyNPgYxhjFU03dYA1NlDGrf3wRr8uOcIHU='

# PATHS----------------------------------------------------

BASE_DIRECTORY = os.getcwd()
API_PREFIX = ''

# DB STATIC CONFIG-----------------------------------------

DB_DRIVERS = {
    'mysql'   : 'mysql',
    'postgres': 'postgres',
    'sqlite'  : 'sqlite'
}
DB_DEFAULT_DRIVER = DB_DRIVERS['postgres']
DB_DRIVER = DB_DRIVERS['postgres']
DB_NAME = 'juju'
DB_HOST = 'localhost'
DB_READ_HOST_NAME = 'localhost'
DB_WRITE_HOST_NAME = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_PREFIX = ''
DB_QUERY_LOGGING = False

# DB CONFIG------------------------------------------------

ORATOR_DATABASES = {
    DB_DRIVER: {
        'driver'  : DB_DRIVER,
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
