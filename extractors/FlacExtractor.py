from typing import Optional

from mutagen.flac import FLAC

from extractors.MediaExtractor import MediaExtractor
from models.TrackMeta import TrackMeta
from util.optional_map import optional_map


class FlacExtractor(MediaExtractor):
    file: FLAC

    def __init__(self, filename: str):
        self.file = FLAC(filename)

    def extract_tag(self, tag: str) -> Optional[str]:
        if tag in self.file.tags:
            for value in self.file.tags[tag]:
                if value is not None:
                    return str(value)
        return None

    def extract_tags(self) -> TrackMeta:
        return TrackMeta(
            album=self.extract_tag('album'),
            albumsort=self.extract_tag('albumsort'),
            albumartist=self.extract_tag('albumartist'),
            albumartistsort=self.extract_tag('albumartistsort'),
            artist=self.extract_tag('artist'),
            artistsort=self.extract_tag('artistsort'),
            catalognumber=self.extract_tag('catalognumber'),
            discnumber=optional_map(self.extract_tag('discnumber'), int),
            disctotal=optional_map(self.extract_tag('disctotal'), int),
            label=self.extract_tag('label'),
            media=self.extract_tag('media'),
            originaldate=self.extract_tag('originaldate'),
            originalyear=self.extract_tag('originalyear'),
            title=self.extract_tag('title'),
            titlesort=self.extract_tag('titlesort'),
            tracknumber=optional_map(self.extract_tag('tracknumber'), int),
            tracktotal=optional_map(self.extract_tag('tracktotal'), int),
        )
