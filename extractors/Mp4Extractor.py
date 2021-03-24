from typing import Optional, Tuple

from mutagen.mp4 import MP4

from extractors.MediaExtractor import MediaExtractor
from models.TrackMeta import TrackMeta
from util.optional_map import optional_map


class Mp4Extractor(MediaExtractor):
    file: MP4

    def __init__(self, filename: str):
        self.file = MP4(filename)

    @staticmethod
    def __convert_media_type(media_id: int) -> str:
        if media_id == 0 or media_id == 9:
            return 'movie'
        if media_id == 1:
            return 'music'
        if media_id == 2:
            return 'audiobook'
        if media_id == 6:
            return "music_video"
        if media_id == 10:
            return 'tv_show'
        if media_id == 11:
            return 'booklet'
        if media_id == 14:
            return 'ringtone'
        else:
            return str(media_id)

    def extract_tag(self, tag: str) -> Optional[str]:
        if tag in self.file.tags:
            for value in self.file.tags[tag]:
                if value is not None:
                    return str(value)
        return None

    def extract_numbers(self, tag: str) -> Optional[Tuple[int, int]]:
        if tag in self.file.tags:
            for value in self.file.tags[tag]:
                if value is not None:
                    return value
        return None

    def extract_tags(self) -> TrackMeta:
        discnumber, disctotal = self.extract_numbers('disk')
        tracknumber, tracktotal = self.extract_numbers('trkn')
        return TrackMeta(
            album=self.extract_tag('\xa9alb'),
            albumsort=self.extract_tag('soal'),
            albumartist=self.extract_tag('aART'),
            albumartistsort=self.extract_tag('soaa'),
            artist=self.extract_tag('\xa9ART'),
            artistsort=self.extract_tag('soar'),
            catalognumber=optional_map(self.extract_tag('----:com.apple.iTunes:CATALOGNUMBER'), str),
            discnumber=discnumber,
            disctotal=disctotal,
            label=optional_map(self.extract_tag('----:com.apple.iTunes:LABEL'), str),
            media=optional_map(self.extract_tag('stik'), self.__convert_media_type),
            originaldate=None,
            originalyear=self.extract_tag('\xa9day'),
            title=self.extract_tag('\xa9nam'),
            titlesort=self.extract_tag('sonm'),
            tracknumber=tracknumber,
            tracktotal=tracktotal,
        )
