import click
import subprocess
from sunkcosts.tokens import auth
from sunkcosts.term import vprint
from sunkcosts.env import VERSION, APP_ENTRY_POINT


@click.group()
@click.version_option(VERSION)
@click.pass_context
def scli(ctx):
    pass


# ! ---


@scli.group()
def tokens():
    "Configure API tokens."
    pass


@tokens.command()
def configured():
    "view configured api keys"
    vprint(auth.tokens)


@tokens.command()
@click.option(
    "--name",
    type=str,
    help="Name of API token.",
    required=True,
)
def view(name: str) -> None:
    "View an API token."
    vprint(auth.get(name))


@tokens.command()
@click.option(
    "--name",
    type=str,
    help="Name of API token.",
    required=True,
)
@click.option(
    "--token",
    type=str,
    help="API token.",
    required=True,
)
def save(name: str, token: str) -> None:
    "Save an API token."
    auth.save(name, token)


@tokens.command()
@click.option(
    "--name",
    type=str,
    help="Name of API token.",
    required=True,
)
def delete(name: str) -> None:
    "Delete an API token from package cache."
    auth.delete(name)


@tokens.command()
@click.option(
    "--name",
    required=True,
)
def copy():
    "copy key to clipboard"
    # TODO
    raise NotImplementedError()


# ! ---


@scli.group()
def model():
    "Model utilities."
    pass


@model.command(name="gui")
@click.option(
    "--browser/--no-browser",
    type=bool,
    default=False,
    help="Automatically open the browser, defaults to false.",
)
@click.option(
    "--run-on-save/--no-run-on-save",
    type=bool,
    default=True,
    help="Rerun the app when file saved, defaults to false.",
)
@click.option(
    "--host",
    type=str,
    default="localhost",
    help="Host path to serve app on, defaults to localhost.",
)
@click.option(
    "--port",
    type=int,
    default=4096,
    help="Port to serve app on, defaults to 4096.",
)
def model_gui(browser: bool, run_on_save: bool, host: str, port: int):
    """Start the model GUI."""
    subprocess.run(
        [
            "streamlit",
            "run",
            APP_ENTRY_POINT,
            "--server.headless",
            "false" if browser else "true",
            "--logger.enableRich",
            "true",
            "--browser.gatherUsageStats",
            "false",
            "--server.runOnSave",
            "true" if run_on_save else "false",
            "--server.address",
            host,
            "--server.port",
            str(int(port)),
            "--theme.primaryColor",
            "#2671c7",
            "--theme.base",
            "dark",
        ]
    )


@model.command(name="forecast")
def model_forecast():
    "Not yet implemented, forecast economic cost on terminal given input parameters."
    raise NotImplementedError()
