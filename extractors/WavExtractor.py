from typing import Optional

from mutagen.wave import WAVE

from extractors.MediaExtractor import MediaExtractor
from models.TrackMeta import TrackMeta
from util.extract_numbers import extract_numbers


class WaveExtractor(MediaExtractor):
    file: WAVE

    def __init__(self, filename: str):
        self.file = WAVE(filename)

    def extract_tag(self, tag: str) -> Optional[str]:
        if tag not in self.file.tags:
            return None
        return str(self.file.tags[tag])

    def extract_tags(self) -> TrackMeta:
        discnumber, disctotal = extract_numbers(self.extract_tag('TPOS'))
        tracknumber, tracktotal = extract_numbers(self.extract_tag('TRCK'))
        return TrackMeta(
            album=self.extract_tag('TALB'),
            albumsort=self.extract_tag('TSOA'),
            albumartist=self.extract_tag('TPE2'),
            albumartistsort=self.extract_tag('TSO2'),
            artist=self.extract_tag('TPE1'),
            artistsort=self.extract_tag('TSOP'),
            catalognumber=self.extract_tag('TXXX:CATALOGNUMBER'),
            discnumber=discnumber,
            disctotal=disctotal,
            label=self.extract_tag('TPUB'),
            media=self.extract_tag('TMED'),
            originaldate=self.extract_tag('TDOR'),
            originalyear=self.extract_tag('TDRC'),
            title=self.extract_tag('TIT2'),
            titlesort=self.extract_tag('TSOT'),
            tracknumber=tracknumber,
            tracktotal=tracktotal,
        )
