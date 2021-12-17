import io

from customio.Output import Output


class OtherOutput(Output):
    file: io.TextIOBase

    def __init__(self, file: io.TextIOBase):
        self.file = file

    def status(self, data: str):
        pass

    def log(self, data: str):
        print(data, file=self.file)
