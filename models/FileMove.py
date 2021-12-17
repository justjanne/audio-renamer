import os

from customio.streams import stdout


class FileMove:
    source: str
    target: str
    intermediate: str

    def __init__(self, source: str, target: str, intermediate: str):
        self.source = source
        self.target = target
        self.intermediate = intermediate

    def move_intermediate(self, dry_run: bool = True):
        if not dry_run:
            if not os.path.exists(self.intermediate):
                os.rename(self.source, self.intermediate)
            else:
                raise Exception("intermediate already exists: {0}".format(self))

    def move_target(self, dry_run: bool = True):
        if dry_run:
            stdout().log("Moving File:")
            stdout().log("  ← {0}".format(self.source))
            stdout().log("  → {0}".format(self.target))
        else:
            target_folder = os.path.dirname(self.target)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            if not os.path.exists(self.target):
                os.rename(self.intermediate, self.target)
            else:
                raise Exception("target already exists: {0}".format(self))

    def __str__(self):
        return "FileMove(source=\'{0}\', target=\'{1}\', intermediate=\'{2}\')" \
            .format(self.source, self.target, self.intermediate)
