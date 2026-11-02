from .models import ContextSeed, ContextSeedRelationship
from Pearl.models import Pearl
from .relationship_generator import ContextSeedRelationshipGenerator

class ContextSeedService:
    @staticmethod
    def create_seed(*, pearl, seed_type, value, confidence=None)->ContextSeed:
        if pearl is None:
            raise ValueError("No pearl provided, pearl is required")
        if not value:
            raise ValueError("Seed Value is required")
        return ContextSeed.objects.create(
            pearl=pearl,
            seed_type=seed_type,
            value=value,
            confidence=confidence
        )

class ContextSeedRelationshipService:
    @staticmethod
    def create_relationship(*, candidate):
        seed_a = candidate.seed_a
        seed_b = candidate.seed_b

        if seed_a.pk == seed_b.pk:
            raise ValueError(
                "A Context Seed cannot have a relationship with itself"
            )

        if seed_a.pk > seed_b.pk:
            seed_a, seed_b = seed_b, seed_a

        relationship, _ = ContextSeedRelationship.objects.get_or_create(
            seed_a = seed_a,
            seed_b = seed_b,
            defaults={
                "relationship_type": candidate.relationship_type,
            },
        )
        return relationship


class ContextSeedRelationshipDiscoveryService:
    @staticmethod
    def discover_and_persist_for_seeds(*, new_seeds):
        new_seeds = list(new_seeds)

        if not new_seeds:
            return []

        # This operation handles Seeds created for one Pearl at a time.
        pearl_ids = {seed.pearl_id for seed in new_seeds}

        if len(pearl_ids) != 1:
            raise ValueError(
                "All new Seeds must belong to the same Pearl."
            )

        relationships = []

        for new_seed in new_seeds:
            existing_seeds = ContextSeed.objects.filter(
                pearl__owner_id=new_seed.pearl.owner_id,
            ).exclude(
                pearl_id=new_seed.pearl_id,
            )

            for existing_seed in existing_seeds:
                candidate = ContextSeedRelationshipGenerator.discover(
                    seed_a=new_seed,
                    seed_b=existing_seed,
                )

                if candidate is None:
                    continue

                relationship = (
                    ContextSeedRelationshipService.create_relationship(
                        candidate=candidate,
                    )
                )

                relationships.append(relationship)

        return relationships