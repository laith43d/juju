import os
from subprocess import call

import click


@click.group()
def cli():
    """
    Api operations.
    :return:
    """
    pass


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

        with open(f'api/{api_name.capitalize()}.py', 'w') as f:
            f.write(f'''

from flask_classful import FlaskView as Resource, route
from models.{api_name.capitalize()} import {api_name.capitalize()}
from flask import jsonify, request

    @route('', methods = ['GET'])
    def all(self):
        return {api_name.capitalize()}.all().to_json()

    @route('/<int:id_>', methods = ['GET'])
    def one(self, id_):
        return {api_name.capitalize()}.find(id_).to_json()

    @route('add', methods = ['POST'])
    def add(self):
        {api_name.capitalize()}.create(**request.get_json())
        return jsonify({'message': '{api_name} added successfully'})

    @route('update/<int:id_>', methods = ['PATCH'])
    def update(self, id_):
        {api_name} = {api_name.capitalize()}.find_or_fail(id_)
        {api_name}.update(**request.get_json())
        return jsonify({api_name}.to_json())

    @route('delete/<int:id_>', methods = ['DELETE'])
    def delete(self, id_):
        {api_name.capitalize()}.destroy(id_)
        return jsonify({'message': '{api_name} deleted successfully'})

''')

        with open(f'api/__init__.py', 'a+') as f:
            f.write(
                f'from api.{api_name.capitalize()} import {api_name.capitalize()}View\n')
            f.write(
                f'{api_name.capitalize()}View.register(app)\n\n')

        click.echo('\033[92mApi Created Successfully!\033[0m')

    else:
        click.echo('\033[95mApi Already Exists!\033[0m')
