from .models import PearlSourceType
from urllib.parse import urlparse
from .exceptions import InvalidCaptureRequest, UnknownSourceType

class SourceTypeDetector:
    @staticmethod
    def detect(value:str) -> PearlSourceType:
        if not value or not value.strip():
            raise ValueError("A value is required for source type detection")
        parsed = urlparse(value)
        if parsed.scheme in  ["http", "https"] and parsed.netloc:
            return PearlSourceType.URL
        return PearlSourceType.TEXT
    # 