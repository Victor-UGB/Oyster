from .seed_generator import ContextSeedGenerator
from .services import ContextSeedService

class ContextSeedGenerationService:
    @staticmethod
    def generate_and_persist(*, pearl, metadata):
        candidates = ContextSeedGenerator.generate(
            pearl = pearl,
            metadata = metadata
        )

        seeds = []

        for candidate in candidates:
            seed = ContextSeedService.create_seed(
                pearl=pearl,
                seed_type=candidate.seed_type,
                value=candidate.value,
                confidence=candidate.confidence
            )
            seeds.append(seed)

        return seeds


