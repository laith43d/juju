import os
from subprocess import call

import click

from manage import cli


@cli.command(name = "make:api")
@click.argument("api_name", required = True)
@click.option("--model", is_flag = True)
def make_api(api_name: str, model):
    """
    Create new api resource view.\n
    :param api_name: api name in singular form.\n
    :param model: optional, create model along with api.\n
    :return: None
    """

    if not os.path.isfile(f'api/{api_name.capitalize()}.py'):

        if model:
            call(['juju', 'db', 'make:model', api_name])

        with open(f'api/{api_name}.py', 'w') as f:
            f.write(f"from flask_classful import FlaskView as Resource, route\n"
                    f"from models.{api_name} import {api_name.capitalize()}\n"
                    f"from flask import request, jsonify\n"
                    f"\n"
                    f"class {api_name.capitalize()}View(Resource):\n"
                    f"    pass")

        with open('api/__init__.py', 'a+') as f:
            f.write(
                f'from api.{api_name} import {api_name.capitalize()}View\n')
            f.write(
                f'{api_name.capitalize()}View.register(app, route_prefix = API_PREFIX)\n\n')

        click.echo('\033[92mApi Created Successfully!\033[0m')

    else:
        click.echo('\033[95mApi Already Exists!\033[0m')
