import os

import click

from manage import cli


@cli.command(name = "make:command")
@click.argument("command_name", required = True)
def make_command(command_name: str):
    """
    Create new command.\n
    :param command_name: command name in singular form.\n
    :return: None
    """

    if not os.path.isfile(f'cli/cmd_{command_name}.py'):

        with open(f'cli/{command_name}.py', 'w') as f:
            f.write(f'''
import click

from manage import cli


@cli.command(name = "{command_name}")
def {command_name}():
    pass
            ''')

        with open(f'cli/__init__.py', 'a+') as f:
            f.write(
                f'from .cmd_{command_name} import *\n')

        click.echo('\033[92mCommand Created Successfully!\033[0m')

    else:
        click.echo('\033[95mCommand Already Exists!\033[0m')
