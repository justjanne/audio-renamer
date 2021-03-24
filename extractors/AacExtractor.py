from typing import Optional

from mutagen.apev2 import APEv2File

from extractors.MediaExtractor import MediaExtractor
from models.TrackMeta import TrackMeta
from util.extract_numbers import extract_numbers


class AacExtractor(MediaExtractor):
    file: APEv2File

    def __init__(self, filename: str):
        self.file = APEv2File(filename)

    def extract_tag(self, tag: str) -> Optional[str]:
        if tag not in self.file.tags:
            return None
        return str(self.file.tags[tag])

    def extract_tags(self) -> TrackMeta:
        discnumber, disctotal = extract_numbers(self.extract_tag('Disc'))
        tracknumber, tracktotal = extract_numbers(self.extract_tag('Track'))
        return TrackMeta(
            album=self.extract_tag('Album'),
            albumsort=self.extract_tag('Albumsort'),
            albumartist=self.extract_tag('Album Artist'),
            albumartistsort=self.extract_tag('Albumartistsort'),
            artist=self.extract_tag('Artist'),
            artistsort=self.extract_tag('Artistsort'),
            catalognumber=self.extract_tag('CatalogNumber'),
            discnumber=discnumber,
            disctotal=disctotal,
            label=self.extract_tag('Label'),
            media=self.extract_tag('Media'),
            originaldate=self.extract_tag('Originaldate'),
            originalyear=self.extract_tag('Originalyear'),
            title=self.extract_tag('Title'),
            titlesort=self.extract_tag('Titlesort'),
            tracknumber=tracknumber,
            tracktotal=tracktotal,
        )
