from .candidates import ContextSeedRelationshipCandidate
from .models import ContextSeedRelationshipType, ConceptualGroupTerm

class ContextSeedRelationshipGenerator:

    @staticmethod
    def discover(*, seed_a, seed_b,):
        if seed_a.pearl_id == seed_b.pearl_id:
            return None

        value_a = seed_a.value.strip().lower()
        value_b = seed_b.value.strip().lower()

        if value_a == value_b:
        
            return ContextSeedRelationshipCandidate(
                seed_a= seed_a,
                seed_b= seed_b,
                relationship_type=ContextSeedRelationshipType.SAME_VALUE
            )

        group_ids = ConceptualGroupTerm.objects.filter(
            normalized_value =value_a
        ).values_list("group_id", flat=True)

        shares_group = ConceptualGroupTerm.objects.filter(
            normalized_value = value_b,
            group_id__in = group_ids
        ).exists()

        if shares_group:
            return ContextSeedRelationshipCandidate(
                seed_a=seed_a,
                seed_b=seed_b,
                relationship_type=ContextSeedRelationshipType.CONCEPTUAL_GROUP
            )

        return None