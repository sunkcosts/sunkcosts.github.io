import os
from typing import Any
from rich.console import Console


def vprint(obj: Any, verbose: bool = True) -> None:
    if verbose:
        Console().print(obj)


def clear():
    os.system("cls" if os.name == "nt" else "clear")
