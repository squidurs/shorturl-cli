from shorturl.commands import *


@click.group()
def cli():
    """CLI for interacting with the URL shortener service."""
    pass

cli.add_command(register)
cli.add_command(login)
cli.add_command(shorten)
cli.add_command(list)
cli.add_command(lookup)
cli.add_command(change_password)

