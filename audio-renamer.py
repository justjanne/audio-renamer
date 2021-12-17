#!/usr/bin/env python3
import argparse
import os
from typing import Iterator, List

from customio.StatusPrinter import StatusPrinter
from customio.streams import stdout
from files.FileFinder import FileFinder
from files.FileMover import FileMover
from models.FileMove import FileMove


def process_folders(folders: List[str]) -> Iterator[FileMove]:
    for foldername in folders:
        stdout().status("Reading folder… {}".format(foldername))
        folder = os.path.abspath(foldername)
        finder = FileFinder(folder)
        mover = FileMover(folder)
        status = StatusPrinter(stdout(), "Reading Files", finder.count())
        for file in finder.all():
            move = mover.move(file)
            status.update(os.path.relpath(file, foldername))
            if move is not None:
                yield move


if __name__ == "__main__":
    stdout().status("Initializing…")
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="+", help="Folders to run the task on")
    parser.add_argument("--dry-run", help="Simulate renames", action="store_true")
    args = parser.parse_args()
    moves = list(process_folders(args.folders))
    statusTmp = StatusPrinter(stdout(), "Creating temporary files", len(moves))
    for move in moves:
        statusTmp.update(move.source)
        move.move_intermediate(args.dry_run)
    statusFinal = StatusPrinter(stdout(), "Writing files", len(moves))
    for move in moves:
        statusTmp.update(move.source)
        move.move_target(args.dry_run)
