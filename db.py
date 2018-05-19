# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
#
# from config.settings import app, db
#
# migrate = Migrate(app, db)
#
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
#
# if __name__ == '__main__':
#     manager.run()

from config.settings import db

if __name__ == '__main__':
    db.cli.run()
