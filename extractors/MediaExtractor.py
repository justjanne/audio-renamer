from typing import Optional

from models.TrackMeta import TrackMeta


class MediaExtractor:
    def extract_tag(self, tag: str) -> Optional[str]:
        """Extract a single tag"""
        pass

    def extract_tags(self) -> Optional[TrackMeta]:
        """Extract media tags from the given file"""
        pass
