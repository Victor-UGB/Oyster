from django.db import transaction
from .models import Pearl, PearlSourceType
from .source_detector import SourceTypeDetector
from .platform_detector import PlatformDetector
from .exceptions import *

class PearlService:
    """
    Domain service responsible for capturing Pearls.
    
    A successful capture guarantees that:

    - A pearl is created
    - The original evidence is preserved exactly as recieved.
    -the owner is recorded.
    - The source type is recorded.
    - The pearl enters the system in a valid state.
    """
    @staticmethod
    @transaction.atomic
    def capture(*,owner, original_value) -> Pearl:
        """
        Capture a new Pearl.

        Args:
            owner:
                The identity that intentionally captured this Pearl.

            source_type:
                The type of source being captured
                (URL, TEXT, IMAGE, DOCUMENT, etc.).

            original_value:
                The original evidence exactly as supplied by the user.
                This value must never be modified before storage.

            source_platform:
                Optional platform the Pearl originated from
                (YouTube, Instagram, GitHub, etc.).

        Returns:
            Pearl:
                The newly created Pearl.

        Raises:
            ValueError:
                If required values are missing.
        """
        if owner is None:
            raise InvalidCaptureRequest("Owner is requied")
        if not original_value or not original_value.strip():
            raise InvalidCaptureRequest
        source_type = SourceTypeDetector.detect(original_value)
        if source_type == PearlSourceType.URL:

            source_platform = PlatformDetector.detect(original_value)
        pearl = Pearl.objects.create(
            owner=owner,
            source_platform=source_platform,
            source_type = source_type,
            original_value=original_value
        )
        print(pearl)

        return pearl
