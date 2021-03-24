from typing import TypeVar, Optional, Callable

T = TypeVar("T")
U = TypeVar("U")


def optional_map(value: Optional[T], function: Callable[[T], U]) -> Optional[U]:
    if value is None:
        return None
    else:
        return function(value)
