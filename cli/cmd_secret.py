import binascii
import os

import click
from manage import cli

@cli.command(name = 'generate:secret')
@click.argument('bytes', default = 128)
def generate_secret(bytes):
    """
    Generate a random secret token.

    :return: str
    """
    return click.echo(binascii.b2a_hex(os.urandom(bytes)))
