import os
from datetime import timedelta

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

BASE_DIRECTORY = os.getcwd()
API_PREFIX = ''
LOG_DIR = os.path.join(BASE_DIRECTORY, 'logs')

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
DB_USERNAME = 'lzah'
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

# JWT -----------------------------------------------------

# Allow browsers to securely persist auth tokens but also include it in the
# headers so that other clients can use the auth token too.
JWT_TOKEN_LOCATION = ['cookies', 'headers']

# Only allow JWT cookies to be sent over https. In production, this should
# likely be True.
JWT_COOKIE_SECURE = False

# When set to False, cookies will persist even after the browser is closed.
JWT_SESSION_COOKIE = False

# Expire tokens in 1 year (this is unrelated to the cookie's duration).
JWT_ACCESS_TOKEN_EXPIRES = timedelta(weeks=52)

# We are authenticating with this auth token for a number of endpoints.
JWT_ACCESS_COOKIE_PATH = '/'

# Enable CSRF double submit protection. See this for a thorough
# explanation: http://www.redotheweb.com/2015/11/09/api-security.html
JWT_COOKIE_CSRF_PROTECT = True
