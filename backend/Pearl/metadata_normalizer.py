class MetadataNomalizer:
    CANONICAL_FIELDS = [
        "title",
        "description",
        "thumbnail",
        "site_name",
    ]
    @staticmethod
    def normalize(raw_metadata: dict)-> dict:
        normalized = {}
        for field in MetadataNomalizer.CANONICAL_FIELDS:
            value = raw_metadata.get(field)
            if isinstance(value, str):
                value = value.strip()
            if value:
                normalized[field] = value
        return normalized