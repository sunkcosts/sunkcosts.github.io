import click
from sunklib.util.auth import credentials
from sunklib.util.term import vprint
from sunklib.env import VERSION


@click.group()
@click.version_option(VERSION)
@click.pass_context
def scli(ctx):
    pass


@scli.group()
def auth():
    pass


@auth.command()
def configured():
    "view configured api keys"
    vprint(credentials.tokens)


@auth.command()
@click.option("--name", type=str, help="Name of API token.")
def view(name: str) -> None:
    "View an API token."
    vprint(credentials.get(name))


@auth.command()
@click.option("--name", type=str, help="Name of API token.")
@click.option("--token", type=str, help="API token.")
def save(name: str, token: str) -> None:
    "Save an API token."
    credentials.save(name, token)


@auth.command()
@click.option("--name", type=str, help="Name of API token.")
def delete(name: str) -> None:
    "Delete an API token from package cache."
    credentials.delete(name)


@auth.command()
@click.option("--name")
def copy():
    "copy key to clipboard"
    # TODO
    raise NotImplementedError()
