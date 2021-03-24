from typing import Tuple, Optional


def extract_numbers(tag: str) -> Tuple[Optional[str], Optional[str]]:
    number = None
    total = None

    split = str(tag).split("/")
    if len(split) >= 1:
        number = int(split[0])
    if len(split) >= 2:
        total = int(split[1])

    return number, total
