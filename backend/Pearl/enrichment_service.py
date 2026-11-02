from dataclasses import dataclass
from .models import Pearl, PearlSourceType
from .metadata_extractor import MetaExtractor
from  .metadata_normalizer import MetadataNomalizer
from .snapshot_service import MetadataSnapshotServices
from .services import PearlService


@dataclass
class EnrichedPearl:
    pearl:Pearl
    metadata: dict
class PearlEnrichmentService:
    
    # Take a captured Pearl
    # Return a structured / enriched dictionary 
    # Using extracted metadat to create this enrichment
    @staticmethod
    def capture_and_enrich(*, owner, original_value)->EnrichedPearl:
        pearl = PearlService.capture(
            owner=owner, 
            original_value=original_value
        )
        print(f"Pearl source type: {pearl.source_type}")

        metadata = {}

        if pearl.source_type == PearlSourceType.URL:
            print("Entering metadata extraction...")

            
            extraction_result= MetaExtractor.extract(original_value)
            print(f"Raw metadata: {extraction_result}")
            if extraction_result.success:
                metadata= MetadataNomalizer.normalize(extraction_result.metadata)
                print(f"Normalized metadata: {metadata}")
                if metadata:
                    MetadataSnapshotServices.create_snapshot(
                        pearl=pearl,
                        metadata=metadata
                    )
                    
           
        print(f"This is the metadata {metadata}")
        return EnrichedPearl(
            pearl=pearl,
            metadata=metadata
        )
  