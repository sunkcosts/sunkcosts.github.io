from typing import Any
from rich.console import Console


def vprint(obj: Any, verbose: bool = True) -> None:
    if verbose:
        Console().print(obj)
