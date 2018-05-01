import os
import sys
import click

BASE_DIR = os.getcwd()
CONTEXT_SETTINGS = dict(auto_envvar_prefix = 'JUJU')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file = sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure = True)
cmd_folder = os.path.join(BASE_DIR + '/cli', 'commands')


class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
                    filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('cli.commands.cmd_' + name, locals = None, globals = None, fromlist = ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls = CLI, context_settings = CONTEXT_SETTINGS)
@click.option('--home', type = click.Path(exists = True, file_okay = False,
                                          resolve_path = True),
              help = 'Changes the folder to operate on.')
@click.option('-v', '--verbose', is_flag = True,
              help = 'Enables verbose mode.')
@pass_context
def cli(ctx, verbose, home):
    """JUJU command line interface."""
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home
