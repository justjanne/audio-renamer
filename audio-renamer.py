#!/usr/bin/env python3
import argparse
import os
from typing import Iterator, List

from files.FileFinder import FileFinder
from files.FileMover import FileMover
from models.FileMove import FileMove


def process_folders(folders: List[str]) -> Iterator[FileMove]:
    for foldername in folders:
        folder = os.path.abspath(foldername)
        finder = FileFinder(folder)
        mover = FileMover(folder)
        for file in finder.all():
            move = mover.move(file)
            if move is not None:
                yield move


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="+", help="Folders to run the task on")
    parser.add_argument("--dry-run", help="Simulate renames", action="store_true")
    args = parser.parse_args()
    moves = list(process_folders(args.folders))
    for move in moves:
        move.move_intermediate(args.dry_run)
    for move in moves:
        move.move_target(args.dry_run)
