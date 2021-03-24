import re
from typing import Optional

from models.FileMeta import FileMeta
from models.TrackMeta import TrackMeta
from util.coalesce import coalesce
from util.optional_map import optional_map

space_re = re.compile(r"  +")


class FileMetaParser:
    def __init__(self, track: TrackMeta):
        self.track = track

    @staticmethod
    def __fix_prefixes(name: str) -> str:
        for prefix in ["A", "The"]:
            prefix_str = "{0} ".format(prefix)
            if name.startswith(prefix_str):
                name = "{0}, {1}".format(
                    name[len(prefix_str):],
                    prefix
                )
        return name

    @staticmethod
    def __sanitize_path(name: str) -> str:
        name = name.replace("...", "…")
        name = name.replace("N°", "No")
        name = name.replace("#", "No ")
        name = name.replace(":", " - ")
        name = name.replace(";", " - ")
        name = name.replace("·", "-")
        name = name.replace("/", " - ")
        name = name.replace("|", " - ")
        name = name.replace("\\", " - ")
        name = name.replace("?", " ")
        name = name.replace("!", " ")
        name = name.replace("×", " x ")
        name = name.replace("*", " ")
        name = name.replace("<", "(")
        name = name.replace(">", ")")
        name = name.replace("\"", "'")
        name = space_re.sub(" ", name)
        name = name.strip()
        return name

    @staticmethod
    def __parse_year(data):
        return int(data.split("-", 1)[0])

    @staticmethod
    def __format_number(number, total):
        if total is None:
            return str(number)
        else:
            return str(number).zfill(len(str(total)))

    def __get_albumartist(self) -> Optional[str]:
        return self.__fix_prefixes(self.__sanitize_path(
            coalesce(self.track.albumartist, self.track.artist, fallback='Unknown Artist')
        ))

    def __get_album(self) -> Optional[str]:
        album = self.__sanitize_path(
            coalesce(self.track.albumsort, self.track.album, fallback='Unknown Album')
        )
        year = optional_map(
            coalesce(self.track.originaldate, self.track.originalyear),
            self.__parse_year
        )

        if album is None:
            return None

        if year is None:
            return album

        return "{0} ({1})".format(album, int(year))

    def __get_track(self) -> Optional[str]:
        title = self.__sanitize_path(coalesce(self.track.title, fallback='Unknown Track')).rstrip(".")
        discnumber = self.track.discnumber
        disctotal = self.track.disctotal
        tracknumber = self.track.tracknumber
        tracktotal = self.track.tracktotal

        if tracknumber is None:
            return title

        if discnumber is None or disctotal is None or disctotal <= 1:
            return "{0}. {1}".format(
                self.__format_number(tracknumber, tracktotal),
                title
            )

        return "{0}-{1}. {2}".format(
            self.__format_number(discnumber, disctotal),
            self.__format_number(tracknumber, tracktotal),
            title,
        )

    def get_meta(self) -> Optional[FileMeta]:
        track = self.__get_track()
        if track is None:
            return None

        return FileMeta(
            album=self.__get_album(),
            albumartist=self.__get_albumartist(),
            track=track
        )
