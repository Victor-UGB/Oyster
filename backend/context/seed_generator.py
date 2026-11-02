from .candidates import ContextSeedCandidate

class ContextSeedGenerator:
    @staticmethod
    def generate(*, pearl, metadata)->list[ContextSeedCandidate]:
        if not metadata:
            return []
        candidates = []

        title = metadata.get("title", "").lower()
        description = metadata.get("description", "").lower()

        text = f"{title} {description}"

        if "electric vehicle" in text or "electric vehicles" in text:
            candidates.append(
                ContextSeedCandidate(
                    seed_type="topic",
                    value="electric vehicles"
                )
            )

        return candidates