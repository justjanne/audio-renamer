from typing import List, Optional

from mutagen.id3 import ID3

from extractors.MediaExtractor import MediaExtractor
from models.TrackMeta import TrackMeta
from util.extract_numbers import extract_numbers


class Mp3Extractor(MediaExtractor):
    file: ID3

    def __init__(self, filename: str):
        self.file = ID3(filename)

    @staticmethod
    def _extract_numbers_mp3(tags: List[str]) -> (List[str], List[str]):
        numbers = []
        totals = []
        for tag in tags:
            split = str(tag).split("/")
            if len(split) > 0:
                numbers.append(split[0])
            if len(split) > 1:
                totals.append(split[1])
        return numbers, totals

    def extract_tag(self, tag: str) -> Optional[str]:
        if tag in self.file:
            for value in self.file.getall(tag):
                if value is not None:
                    return str(value)
        return None

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
