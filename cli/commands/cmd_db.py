import os
from subprocess import call

import click


@click.group()
def cli():
    """
    DB operations.
    """
    pass


@cli.command(name = 'make:migration')
@click.argument('migration_name', required = True)
@click.option('--table', default = False)
@click.option('--create', is_flag = True)
@click.option('--model', is_flag = True)
@click.option('--api', is_flag = True)
def make_migration(migration_name: str, table, create, model, api):
    """
    Creates a migration files.\n
    :param migration_name: each migration should assigned a unique name.\n
    :param table: database table.\n
    :param create: if you want to create a db table, set this option.\n
    :param model: would you like to create the associative model?\n
    :param api: create associative Api\n
    :return: None
    """
    if api:
        call(['juju', 'api', 'make:api', migration_name.capitalize()])
    if model:
        call(['juju', 'db', 'make:model', migration_name.capitalize()])
    if create:
        call(['python', 'db.py', 'make:migration', migration_name,
              '-p', 'migrations', '--table', table, '--create'])
    elif table:
        call(['python', 'db.py', 'make:migration', migration_name,
              '-p', 'migrations', '--table', table])
    else:
        call(['python', 'db.py', 'make:migration', migration_name,
              '-p', 'migrations'])


@cli.command(name = "migrate:refresh")
def migration_refresh():
    """
     Rolls back migrations and remigrates.\n
    :return: None
    """
    call(['python', 'db.py', 'migrate:refresh', '-p', 'migrations', '-f'])


@cli.command()
def migrate():
    """
    Run migration.
    :return:
    """
    call(['python', 'db.py', 'migrate', '-p', 'migrations', '-f'])


@cli.command(name = "migrate:reset")
def migration_reset():
    """
     Rolls back latest migration operation.\n
    :return: None
    """
    call(['python', 'db.py', 'migrate:reset', '-p', 'migrations', '-f'])


@cli.command(name = "migrate:rollback")
def migration_rollback():
    """
     Undo all migrations.\n
    :return: None
    """
    call(['python', 'db.py', 'migrate:rollback', '-p', 'migrations', '-f'])


@cli.command(name = "migrate:status")
def migration_status():
    """
     Migration status.\n
    :return: None
    """
    call(['python', 'db.py', 'migrate:status'])


@cli.command(name = "make:seed")
@click.argument('seed_name', required = True)
def make_seed(seed_name):
    """
    Make seed.\n
    :param seed_name: seed name must make sense and relevant to your tables/migrations\n
    :return: None
    """
    call(['python', 'db.py', 'make:seed', '-p', 'seeds', seed_name])


@cli.command(name = "db:seed")
@click.argument('seed_name', required = False)
def db_seed(seed_name):
    """
    Run seed/s.\n
    :param seed_name: provide seed name to run specific seed, otherwise will run all seeds.\n
    :return: None
    """
    call(['python', 'db.py', 'db:seed', '-p', 'seeds', seed_name])


@cli.command(name = "seed:refresh")
def db_seed():
    """
    Run migrate:refresh with seed/s.\n
    :return: None
    """
    call(['python', 'db.py', 'migrate:refresh', '--seed'])


@cli.command(name = "make:model")
@click.argument('model_name', required = True)
@click.option('--migration', is_flag = True)
def make_model(model_name: str, migration):
    """
    Create model.\n
    :param model_name: model name in singular form.\n
    :param migration: if you would like to create migration as well\n
    :return: None
    """
    if migration:
        call(['python', 'db.py', 'make:migration', model_name,
              '-p', 'migrations', '--table', model_name, '--create'])

    if not os.path.isfile(f'models/{model_name.capitalize()}.py'):

        with open(f'models/{model_name.capitalize()}.py', 'w') as f:
            f.write(f'''
from config.settings import Model


class {model_name.capitalize()}(Model):
    pass
''')

        with open(f'models/__init__.py', 'a+') as f:
            f.write(
                f'from models.{model_name.capitalize()} import {model_name.capitalize()}\n')

        click.echo('\033[92mModel Created Successfully!\033[0m')

    else:
        click.echo('\033[95mModel Already Exists!\033[0m')
