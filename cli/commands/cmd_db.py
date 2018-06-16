import os

import click


@click.group()
def cli():
    """
    Make a new model.
    """
    pass


@cli.command(name = "make:model")
@click.argument('model_name', required = True)
def make_model(model_name: str):
    """
    Create model.\n
    :param model_name: model name in singular form.\n
    :param migration: if you would like to create migration as well\n
    :return: None
    """
    if not os.path.isfile(f'models/{model_name}.py'):

        with open(f'models/{model_name}.py', 'w') as f:
            f.write(f'''
from config.settings import Model
from facilities.databases.DBMixins import IDMixin


class {model_name.capitalize()}(Model, IDMixin):
    pass
''')

        with open(f'models/__init__.py', 'a+') as f:
            f.write(
                f'from models.{model_name} import {model_name.capitalize()}\n')

        click.echo('\033[92mModel Created Successfully!\033[0m')

    else:
        click.echo('\033[95mModel Already Exists!\033[0m')
