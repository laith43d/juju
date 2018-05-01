from subprocess import call

# from time import sleep
import click


@click.command()
def cli():
    """
    Install project requirements.
    :return: None
    """

    # call(['python3', '-m', 'venv', 'venv'])
    # sleep(5)
    call(['pip3', 'install', '-r', 'requirements.txt'])
    print("INFO: Installed all requirements successfully")
    call(['pip3', 'install', '--editable', '.'])
