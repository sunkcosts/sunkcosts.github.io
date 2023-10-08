import click
from sunklib.env import VERSION


@click.group()
@click.version_option(VERSION)
@click.pass_context
def SCLI(ctx):
    pass


@click.group()
def auth():
    pass


@auth.command()
@click.option("--name")
def view():
    "view api keys"
    pass


@auth.command()
@click.option("--name")
@click.option("--key")
def save():
    "save api keys"
    pass


@auth.command()
@click.option("--name")
def copy():
    "copy key to clipboard"
    pass


@auth.command()
@click.option("--name")
def delete():
    "delete an api key from memory"
    pass


@auth.command()
@click.option("--name")
@click.option("--key")
def add():
    pass


# set data directory

# set API keys
