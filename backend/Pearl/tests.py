from django.test import TestCase
from unittest.mock import patch
from .services import PearlService
from .models import Pearl, PearlSourceType
from .source_detector import SourceTypeDetector
from .platform_detector import PlatformDetector
from .metadata_extractor import MetaExtractor, ExtractionResult
from .enrichment_service import PearlEnrichmentService, EnrichedPearl
from .metadata_normalizer import MetadataNomalizer
from .snapshot_service import MetadataSnapshot
from django.contrib.auth import get_user_model
from .exceptions import InvalidCaptureRequest




class MetadataSnapshotTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="victor",
            password="password123"
        )

    def test_enrichment_creates_metadata_snapshot(self):

        result = PearlEnrichmentService.capture_and_enrich(
            owner=self.user,
            original_value="https://github.com/openai/openai-python"
        )

        self.assertEqual(
            MetadataSnapshot.objects.count(),
            1
        )

        snapshot = MetadataSnapshot.objects.first()

        self.assertEqual(
            snapshot.pearl,
            result.pearl
        )

        self.assertIn(
            "title",
            snapshot.metadata
        )

class MetadataNormalizerTest(TestCase):
    def test_normalizes_metadata(self):
        raw_metadata = {
            "title": "  OpenAI Python SDK  ",
            "description": " Official Python library ",
            "thumbnail": "https://example.com/image.png",
            "site_name": " GitHub ",
        }
        result = MetadataNomalizer.normalize(raw_metadata)
        self.assertEqual(result["title"],"OpenAI Python SDK" )
        self.assertEqual(result["site_name"], "GitHub")

    def test_removes_empty_values(self):
        raw_metadata = {
            "title": "Useful Article",
            "description": "",
            "thumbnail": None,
        }
        normalized = MetadataNomalizer.normalize(raw_metadata)
        self.assertEqual(normalized, {"title": "Useful Article"})

    def test_removes_unknown_fields(self):
        raw_metadata = {
            "title": "Useful Article",
            "author": "Victor",
            "likes": 100,
        }
        normalized = MetadataNomalizer.normalize(raw_metadata)
        self.assertEqual(normalized, {"title": "Useful Article"})
    
class PearlEnrichmentTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Victor Itodo",
            password="password1"
        )
    def test_enriched_pearl_is_returned(self):
        result = PearlEnrichmentService.capture_and_enrich(
            owner=self.user,
            original_value = "https://github.com/openai/openai-python"
        )
        self.assertIsInstance(result, EnrichedPearl)
        self.assertEqual(result.pearl.owner, self.user)
        self.assertEqual(result.pearl.source_type, PearlSourceType.URL)
        self.assertIn("title", result.metadata)
        self.assertIn("description", result.metadata)
        self.assertIn("site_name", result.metadata)
    def capture_and_enrich_with_github_url(self):
        result = PearlEnrichmentService.capture_and_enrich(
            owner=self.user,
            original_value="https://github.com/openai/openai-python"
        )
        self.assertEqual(result.pearl.source_platform, "GitHub")
        self.assertIn("title", result.metadata)

    def test_capture_and_enrich_creates_snapshot(self):
        extraction_result = ExtractionResult(
            success=True,
            metadata={
                "title": "Test Pearl",
                "description": "Test description",
                "thumbnail": "https://example.com/image.jpg",
                "site_name": "Test Site",
            },
            reason=None,
        )

        with patch(
            "Pearl.enrichment_service.MetaExtractor.extract",
            return_value=extraction_result,
        ):
            result = PearlEnrichmentService.capture_and_enrich(
                owner=self.user,
                original_value="https://example.com/test",
            )

        self.assertEqual(MetadataSnapshot.objects.count(), 1)

        snapshot = MetadataSnapshot.objects.first()

        self.assertEqual(snapshot.pearl, result.pearl)
        self.assertEqual(snapshot.metadata, result.metadata)

    def test_capture_and_enrich_does_not_create_snapshot_when_metadata_is_unavailable(self):
        extraction_result = ExtractionResult(
            success=False,
            metadata={},
            reason="No OpenGraph metadata found",
        )

        with patch(
            "Pearl.enrichment_service.MetaExtractor.extract",
            return_value=extraction_result,
        ):
            result = PearlEnrichmentService.capture_and_enrich(
                owner=self.user,
                original_value="https://instagram.com/example",
            )

        self.assertEqual(MetadataSnapshot.objects.count(), 0)
        self.assertEqual(result.metadata, {})
        

class MetadataExtractorTest(TestCase):
    def test_extract_returns_metadata_structure(self):
        extract_result = MetaExtractor.extract(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
        self.assertIn("title", extract_result.metadata)
        self.assertIn("description", extract_result.metadata)
        self.assertIn("thumbnail", extract_result.metadata)
        self.assertIn("site_name", extract_result.metadata)
class PlatformDetectorTest(TestCase):
    def test_detects_youtube(self):
        platform = PlatformDetector.detect(
            "https://youtube.com/watch?v=123"
        )
        self.assertEqual(platform, "YouTube")

class SourceTypedetectorTests(TestCase):
    def test_detects_url(self):
        source_type = SourceTypeDetector.detect(
            "https://youtube.com/watch?v=123"
        )
        self.assertEqual(source_type, PearlSourceType.URL)
        print("test sourcetype detector detects url")

    def test_detects_text(self):
        source_type = SourceTypeDetector.detect(
            "This is an important idea"
        )
        self.assertEqual(source_type, PearlSourceType.TEXT)
        print("test sourcetype detector detects text")


class PearlCaptuteTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Victor Itodo",
            password="password1"
        )

    def test_capture_creates_pearl(self):
        pearl = PearlService.capture(
            owner=self.user,
            original_value="https://youtube.com/watch?v=123456"
        )
        self.assertEqual(Pearl.objects.count(), 1)
        self.assertEqual(pearl.owner, self.user)
        self.assertEqual(pearl.source_type, PearlSourceType.URL)
        self.assertEqual(pearl.source_platform, "YouTube")
        self.assertEqual(pearl.original_value, "https://youtube.com/watch?v=123456")
        print("test capture creates pearl passed")

    def test_capture_requires_owner(self):
        with self.assertRaises(InvalidCaptureRequest):
            PearlService.capture(
            owner=None,
            
            original_value="https://youtube.com/watch?v=123456"
        )
        print("test capture requires owner passed")

    def test_capture_detects_platform(self):
        pearl = PearlService.capture(
            owner=self.user,
            original_value="https://youtube.com/watch?v=123456"
        )
        self.assertEqual(pearl.source_platform, "YouTube")

    def test_requires_original_value(self):
        with self.assertRaises(InvalidCaptureRequest):
            PearlService.capture(
                owner=self.user,
                
                original_value=None
            )
            print("test capture requires original value")

    def test_capture_detects_url_and_platform(self):
        pearl = PearlService.capture(
            owner=self.user,
            original_value="https://www.youtube.com/watch?v=abc123"
        )
        self.assertEqual(pearl.source_platform, "YouTube")
        self.assertEqual(pearl.source_type, PearlSourceType.URL)
        self.assertEqual(pearl.original_value, "https://www.youtube.com/watch?v=abc123")