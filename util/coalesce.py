from typing import Optional, TypeVar

T = TypeVar("T")


def coalesce(*args: Optional[T], fallback: T = None) -> T:
    for arg in args:
        if arg is not None:
            return arg
    return fallback
