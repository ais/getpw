import click
from pyperclip import copy

import getpw
from getpw.models import (
    radices,
    functions,
    Props,
)

sradices = sorted(map(str, radices))
sfunctions = sorted(functions)


@click.command()
@click.argument('site')
@click.option('--max_chars',
    type=click.INT,
    default=Props.DEFAULTS.get('max_chars'))
@click.option('--radix',
    type=click.Choice(sradices),
    default=str(Props.DEFAULTS.get('radix')))
@click.option('--function',
    type=click.Choice(sfunctions, case_sensitive=False),
    default=Props.DEFAULTS.get('function'))
@click.option('--ss64',
    type=click.BOOL,
    default=Props.DEFAULTS.get('use_ss64'))
@click.option('--master', prompt=True, hide_input=True)
def main(site:str, max_chars:int, radix:str, function:str, master:str, ss64:bool):
    radix = int(radix)  # Workaround for `str.join` in `click.Choice`
    props = Props(function, max_chars, radix, ss64)

    p = getpw.getpw(master, site, props)
    if p[1] is None:
        raise click.exceptions.UsageError(p[0])
    copy(p[1].decode())

    v = getpw.get_verification_code(master)
    click.echo('Verification code: ' + v.decode())


def run():  main.main()


if __name__ == '__main__':
    run()
