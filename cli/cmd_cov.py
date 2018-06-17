import subprocess

import click
from manage import cli


@click.command(name = 'make:cov')
@click.argument('path', default='tests')
def cli(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
