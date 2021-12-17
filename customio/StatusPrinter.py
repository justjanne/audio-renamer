from customio import Output


class StatusPrinter:
    task: str
    index: int
    total: int

    def __init__(self, output: Output, task: str, total: int):
        self.output = output
        self.task = task
        self.index = 0
        self.total = total

    def update(self, file: str):
        data = self.task + '… '
        if self.total != 0:
            data += "{} / {} ".format(self.index, self.total)
        if file != '':
            data += str(file)
        self.output.status(data)
        self.index += 1
