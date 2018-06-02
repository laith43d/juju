import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config.settings import app, db

migrate = Migrate(app, db, directory = os.path.join(os.getcwd() + '/db/migrations'))

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

