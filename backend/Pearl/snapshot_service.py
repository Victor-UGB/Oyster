from .models import Pearl, MetadataSnapshot
from django.db import transaction


class MetadataSnapshotServices:
    @staticmethod
    @transaction.atomic
    def create_snapshot(*, pearl:Pearl, metadata:dict)->MetadataSnapshot:
        if pearl is None:
            raise ValueError("pearl is required")
        if not metadata:
            return ValueError("metadata is required")
        return MetadataSnapshot.objects.create(
            pearl = pearl,
            metadata = metadata
        )
            