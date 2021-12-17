import os
from typing import Iterator


class FileFinder:
    folder: str

    def __init__(self, folder: str):
        self.folder = folder

    def all(self) -> Iterator[str]:
        for subdir, dirs, files in os.walk(self.folder):
            for filename in files:
                yield os.path.join(self.folder, subdir, filename)

    def count(self) -> int:
        count = 0
        for subdir, dirs, files in os.walk(self.folder):
            count += len(files)
        return count
