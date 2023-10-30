from pathlib import Path
from importlib import metadata
from sunkcosts.io import save_toml


# change name
VERSION = metadata.version("sunklib")


AA_BOUNDS = {
    "top_left": {
        "lat": 25.920,
        "lon": -80.350,
    },
    "bottom_right": {
        "lat": 25.655,
        "lon": -80.060,
    },
}

PATH_HOME = Path.home()
# change name
PATH_CACHE = PATH_HOME / ".sunklib"

PATH_PACKAGE = Path(__file__).parent
PATH_WORKDIR = PATH_PACKAGE.parent
PATH_CACHE_DATA = PATH_WORKDIR / "data"
PATH_DATA_RAW = DR = PATH_CACHE_DATA / "raw"
PATH_DATA_CLEAN = DC = PATH_CACHE_DATA / "clean"
PATH_SITE = PATH_WORKDIR / "report"

FILE_CREDENTIALS = PATH_CACHE / "credentials.toml"

APP_ENTRY_POINT = PATH_PACKAGE / "app" / "main.py"

if not PATH_CACHE.exists():
    PATH_CACHE.mkdir(exist_ok=True)
if not PATH_CACHE_DATA.exists():
    PATH_CACHE_DATA.mkdir(exist_ok=True)
if not FILE_CREDENTIALS.exists():
    save_toml(dict(), FILE_CREDENTIALS)
