from flask.cli import FlaskGroup
from flask_migrate import Migrate

from config.settings import app, db

m = Migrate()
m.init_app(app, db)

cli = FlaskGroup(app)

from cli import *


if __name__ == '__main__':
    cli()

