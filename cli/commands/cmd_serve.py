import click

from config.settings import app


@click.group()
def cli():
    """
    Serves the application for testing locally. If you want to test it
    in a production like environment, please deploy with Docker.
    :return: Application instance
    """
    pass


@cli.command(name = 'serve')
def serve():
    click.echo('\033[95mINFO: Starting the app..\033[0m')
    app.run()
