import os
from subprocess import call
import click


@click.command()
@click.argument('path', default=os.path.join('juju', 'tests'))
def cli(path):
    """
    Run tests with Pytest.

    :param path: Test path
    :return: Subprocess call result
    """
    cmd = 'py.test {0}'.format(path)
    return call(cmd, shell=True)
