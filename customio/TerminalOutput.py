import io
import shutil

from urwid import str_util

from customio.Output import Output


class TerminalOutput(Output):
    file: io.TextIOBase

    def __init__(self, file: io.TextIOBase):
        self.file = file

    def status(self, text: str):
        print("\x1B[K", end='')
        print(TerminalOutput.__truncate_terminal(text), end='\r', flush=True, file=self.file)

    def log(self, data: str, error: bool = False):
        if self.file.isatty():
            print("\x1B[K", end="", file=self.file)
            if error:
                print("\x1B[1;31m", end="", file=self.file)
        print(data, file=self.file)

    @staticmethod
    def __truncate_terminal(text: str) -> str:
        columns = shutil.get_terminal_size((-1, -1)).columns
        if columns <= 0:
            return text
        else:
            return TerminalOutput.__truncate_width(text, columns)

    @staticmethod
    def __truncate_width(text, length):
        result = ""
        width = 0
        for char in text:
            charwidth = str_util.get_width(ord(char))
            if width + charwidth >= length:
                break
            result += char
            width += charwidth
        return result
