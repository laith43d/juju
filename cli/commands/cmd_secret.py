import binascii
import os

import click


@click.command()
@click.argument('bytes', default = 128)
def cli(bytes):
    """
    Generate a random secret token.

    :return: str
    """
    return click.echo(binascii.b2a_hex(os.urandom(bytes)))
