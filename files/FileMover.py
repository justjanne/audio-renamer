import os
from typing import Optional
from uuid import uuid4

from extractors.get_extractor import get_extractor
from files.FileMetaParser import FileMetaParser
from models.FileMeta import FileMeta
from models.FileMove import FileMove


class FileMover:
    folder: str

    def __init__(self, folder: str):
        self.folder = folder

    def __get_target_path(self, name: str, meta: FileMeta) -> str:
        _, extension = os.path.splitext(name)
        path_parts = []
        if meta.albumartist is not None:
            path_parts.append(meta.albumartist)
        if meta.album is not None:
            path_parts.append(meta.album)
        path_parts.append("{0}{1}".format(
            meta.track,
            extension
        ))

        return os.path.join(self.folder, *path_parts)

    def __get_intermediate_path(self, name: str) -> str:
        _, extension = os.path.splitext(name)
        return os.path.join(self.folder, "{0}{1}".format(
            uuid4(),
            extension
        ))

    def move(self, name: str) -> Optional[FileMove]:
        extractor = get_extractor(name)
        if extractor is None:
            print("No Extractor for file: {0}".format(name))
            return None
        track_meta = extractor.extract_tags()
        if track_meta is None:
            print("No Metadata for file: {0}".format(name))
            return None
        file_meta = FileMetaParser(track_meta).get_meta()
        if file_meta is None:
            print("Metadata for file not valid: {0}".format(name))
            return None

        target = self.__get_target_path(name, file_meta)
        if os.path.abspath(name) == os.path.abspath(target):
            return None

        return FileMove(
            name,
            target,
            self.__get_intermediate_path(name)
        )
