from dataclasses import dataclass
from .models import ContextSeed

@dataclass
class ContextSeedCandidate:
    seed_type: str
    value: str
    confidence: float|None = None


@dataclass
class ContextSeedRelationshipCandidate:
    seed_a: ContextSeed
    seed_b: ContextSeed
    relationship_type: str