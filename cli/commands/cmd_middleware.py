import os

import click


@click.group()
def cli():
    """
    Create a new middleware.
    :return:
    """
    pass


@cli.command(name = 'make:middleware')
@click.argument('middleware_name', required = True)
def make_middleware(middleware_name):
    if not os.path.isfile(f'facilities/middleware/{middleware_name}.py'):
        with open(f'facilities/middleware/{middleware_name}.py', 'w') as f:
            f.write(f'from functools import wraps\n'
                    f'\n'
                    f'\n'
                    f'def {middleware_name}(f):\n'
                    f'    @wraps(f)\n'
                    f'    def wrapper(*args, **kwargs):\n'
                    f'        pass\n'
                    f'\n'
                    f'        return f(*args, **kwargs)\n'
                    f'\n'
                    f'    return wrapper\n')

        click.echo('\033[92mMiddleware Created Successfully!\033[0m')

    else:
        click.echo('\033[95mMiddleware Already Exists!\033[0m')
