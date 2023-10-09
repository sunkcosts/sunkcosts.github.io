from pathlib import Path
from importlib import metadata
from sunklib.util.io import save_toml


VERSION = metadata.version("sunklib")

PATH_HOME = Path.home()
PATH_PACKAGE = PATH_HOME / ".sunklib"
FILE_CREDENTIALS = PATH_PACKAGE / "credentials.toml"

if not PATH_PACKAGE.exists():
    PATH_PACKAGE.mkdir(exist_ok=True)
if not FILE_CREDENTIALS.exists():
    save_toml(dict(), FILE_CREDENTIALS)
