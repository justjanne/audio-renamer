import io
import sys

from customio.Output import Output
from customio.OtherOutput import OtherOutput
from customio.TerminalOutput import TerminalOutput


def get_output(target: io.TextIOBase) -> Output:
    if target.isatty():
        return TerminalOutput(target)
    else:
        return OtherOutput(target)


def stdout():
    # noinspection PyTypeChecker
    return get_output(sys.stdout)


def stderr():
    # noinspection PyTypeChecker
    return get_output(sys.stderr)
