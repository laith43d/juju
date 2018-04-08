from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_marshmallow import Marshmallow
from flask_orator import Orator

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

# DB INIT -------------------------------------------------

db = Orator(app)

# db = Database()
#
# db.bind(provider=cfg.DB_DRIVER, host=cfg.DB_HOST, user=cfg.DB_USERNAME, passwd=cfg.DB_PASSWORD, db=cfg.DB_NAME)
# db.generate_mapping(create_tables = True)

# REGISTERED Api-------------------------------------------
from api.User import UserView

UserView.register(app)
