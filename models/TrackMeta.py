from typing import Optional

from util.auto_str import auto_str


@auto_str
class TrackMeta:
    album: Optional[str]
    albumsort: Optional[str]
    albumartist: Optional[str]
    albumartistsort: Optional[str]
    artist: Optional[str]
    artistsort: Optional[str]
    catalognumber: Optional[str]
    discnumber: Optional[int]
    disctotal: Optional[int]
    label: Optional[str]
    media: Optional[str]
    originaldate: Optional[str]
    originalyear: Optional[str]
    title: Optional[str]
    titlesort: Optional[str]
    tracknumber: Optional[str]
    tracktotal: Optional[str]

    def __init__(self,
                 album: Optional[str],
                 albumsort: Optional[str],
                 albumartist: Optional[str],
                 albumartistsort: Optional[str],
                 artist: Optional[str],
                 artistsort: Optional[str],
                 catalognumber: Optional[str],
                 discnumber: Optional[int],
                 disctotal: Optional[int],
                 label: Optional[str],
                 media: Optional[str],
                 originaldate: Optional[str],
                 originalyear: Optional[str],
                 title: Optional[str],
                 titlesort: Optional[str],
                 tracknumber: Optional[int],
                 tracktotal: Optional[int]):
        self.album = album
        self.albumsort = albumsort
        self.albumartist = albumartist
        self.albumartistsort = albumartistsort
        self.artist = artist
        self.artistsort = artistsort
        self.catalognumber = catalognumber
        self.discnumber = discnumber
        self.disctotal = disctotal
        self.label = label
        self.media = media
        self.originaldate = originaldate
        self.originalyear = originalyear
        self.title = title
        self.titlesort = titlesort
        self.tracknumber = tracknumber
        self.tracktotal = tracktotal
