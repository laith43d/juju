import os
from subprocess import call

import click


@click.group()
def cli():
    """
    DB operations.
    """
    pass


@cli.command(name = "make:model")
@click.argument('model_name', required = True)
def make_model(model_name: str, migration):
    """
    Create model.\n
    :param model_name: model name in singular form.\n
    :param migration: if you would like to create migration as well\n
    :return: None
    """
    if not os.path.isfile(f'db/models/{model_name.capitalize()}.py'):

        with open(f'db/models/{model_name.capitalize()}.py', 'w') as f:
            f.write(f'''
from config.settings import Model


class {model_name.capitalize()}(Model):
    pass
''')

        with open(f'models/__init__.py', 'a+') as f:
            f.write(
                f'from db.models.{model_name.capitalize()} import {model_name.capitalize()}\n')

        click.echo('\033[92mModel Created Successfully!\033[0m')

    else:
        click.echo('\033[95mModel Already Exists!\033[0m')
