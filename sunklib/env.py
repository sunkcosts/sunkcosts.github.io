from pathlib import Path
from importlib import metadata
from sunklib.util.io import save_toml


VERSION = metadata.version("sunklib")

PATH_HOME = Path.home()
PATH_CACHE = PATH_HOME / ".sunklib"
PATH_PACKAGE = Path(__file__).parent

FILE_CREDENTIALS = PATH_CACHE / "credentials.toml"

APP_ENTRY_POINT = PATH_PACKAGE / "app" / "main.py"

if not PATH_CACHE.exists():
    PATH_CACHE.mkdir(exist_ok=True)
if not FILE_CREDENTIALS.exists():
    save_toml(dict(), FILE_CREDENTIALS)
