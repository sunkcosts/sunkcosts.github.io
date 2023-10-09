import click
import subprocess
from sunklib.util.auth import credentials
from sunklib.util.term import vprint
from sunklib.env import VERSION, APP_ENTRY_POINT


@click.group()
@click.version_option(VERSION)
@click.pass_context
def scli(ctx):
    pass


# ! ---


@scli.group()
def auth():
    "Configure API tokens."
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
