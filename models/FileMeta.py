from typing import NamedTuple, Optional


class FileMeta(NamedTuple):
    albumartist: Optional[str]
    album: Optional[str]
    track: str

    def __init(self, albumartist, album, track):
        self.albumartist = albumartist
        self.album = album
        self.track = track
