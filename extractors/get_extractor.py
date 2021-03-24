import os
from typing import Optional

from extractors.AacExtractor import AacExtractor
from extractors.FlacExtractor import FlacExtractor
from extractors.MediaExtractor import MediaExtractor
from extractors.Mp3Extractor import Mp3Extractor
from extractors.Mp4Extractor import Mp4Extractor


def get_extractor(filename) -> Optional[MediaExtractor]:
    if os.path.getsize(filename) == 0:
        return None
    if filename.endswith(".flac"):
        return FlacExtractor(filename)
    elif filename.endswith(".mp3"):
        return Mp3Extractor(filename)
    elif filename.endswith(".aac") or filename.endswith(".aac"):
        return AacExtractor(filename)
    elif filename.endswith(".mp4") or filename.endswith(".m4a"):
        return Mp4Extractor(filename)
    else:
        return None
