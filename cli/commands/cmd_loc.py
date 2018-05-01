
from subprocess import check_output

import click


def count_locs(file_type, comment_pattern):
    """
    Detect if a program is on the system path.

    :param file_type: Which file type will be searched?
    :param file_type: str
    :param comment_pattern: Escaped characters that are comments
    :param comment_pattern: str
    :return: str
    """
    find = "find . -name '*.{0}' -print0".format(file_type)
    sed_pattern = "'/^\s*{0}/d;/^\s*$/d'".format(comment_pattern)

    cmd = "{0} | xargs -0 sed {1} | wc -l".format(find, sed_pattern)

    return check_output(cmd, shell = True).decode('utf-8').replace('\n', '')


@click.command()
def cli():
    """
    Count lines of code in the project.

    :return: None
    """
    file_types = (
        ['Python', 'py', '#'],
        ['HTML', 'html', '<!--'],
        ['CSS', 'css', '\/\*'],
        ['JS', 'js', '\/\/']
    )

    click.echo('Lines of code\n-------------')

    for file_type in file_types:
        click.echo("{0}: {1}".format(file_type[0], count_locs(file_type[1],
                                                              file_type[2])))

    return None
