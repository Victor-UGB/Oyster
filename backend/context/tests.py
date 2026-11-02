from django.test import TestCase
from Pearl.models import Pearl
from .models import ContextSeed, Context, ContextPearl, ContextPearlSource, ContextSeedRelationship, ContextSeedRelationshipType, ConceptualGroup, ConceptualGroupTerm
from .services import ContextSeedService, ContextSeedRelationshipService
from .seed_generator import ContextSeedGenerator
from .candidates import ContextSeedCandidate, ContextSeedRelationshipCandidate
from .seed_generation_service import ContextSeedGenerationService
from .relationship_generator import ContextSeedRelationshipGenerator
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction


# Create your tests here.

class ConceptualGroupModelTest(TestCase):
    def test_create_conceptual_group(self):
        group = ConceptualGroup.objects.create(
            name = "Electric Mobility",
            description = "Concepts related to electric mobility"
        )

        self.assertEqual(ConceptualGroup.objects.count(), 1)
        self.assertEqual(group.name, "Electric Mobility")
        self.assertEqual(
            group.description,
            "Concepts related to electric mobility",
        )
        self.assertIsNotNone(group.id)
        self.assertIsNotNone(group.created_at)
        self.assertIsNotNone(group.updated_at)

    def test_conceptual_group_string_representation(self):
        group = ConceptualGroup.objects.create(
            name = "Electric Mobility"
        )

        self.assertEqual(str(group), "Electric Mobility")

    def test_conceptual_group_orders_by_name(self):
        ConceptualGroup.objects.create(name="Real Estate")
        ConceptualGroup.objects.create(name="Electric Mobility")

        groups = list(ConceptualGroup.objects.all())

        self.assertEqual(
            [group.name for group in groups],
            ["Real Estate", "Electric Mobility"],
        )

class ConceptualGroupTermModelTests(TestCase):
    def setUp(self):
        self.group = ConceptualGroup.objects.create(
            name = "Electric mobility"
        )

    def test_create_conceptual_group_term(self):
        term = ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        self.assertEqual(term.group, self.group)
        self.assertEqual(term.value, "Electric Vehicles")
        self.assertEqual(
            term.normalized_value,
            "electric vehicles",
        )
        self.assertIsNotNone(term.id)
        self.assertIsNotNone(term.created_at)

    def test_group_can_have_multiple_terms(self):
        ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )
        ConceptualGroupTerm.objects.create(
            group=self.group,
            value="EV Charging",
            normalized_value="ev charging",
        )

        self.assertEqual(self.group.terms.count(), 2)

    def test_group_rejects_duplicate_normalized_terms(self):
        ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ConceptualGroupTerm.objects.create(
                    group=self.group,
                    value="electric vehicles",
                    normalized_value="electric vehicles",
                )


    def test_same_normalized_term_can_belong_to_different_groups(self):
        another_group = ConceptualGroup.objects.create(
            name="Sustainable Transport",
        )

        ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        ConceptualGroupTerm.objects.create(
            group=another_group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        self.assertEqual(
            ConceptualGroupTerm.objects.filter(
                normalized_value="electric vehicles",
            ).count(),
            2,
        )

    def test_deleting_group_deletes_its_terms(self):
        term = ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        self.group.delete()

        self.assertFalse(
            ConceptualGroupTerm.objects.filter(pk=term.pk).exists()
        )

    def test_term_string_representation(self):
        term = ConceptualGroupTerm.objects.create(
            group=self.group,
            value="Electric Vehicles",
            normalized_value="electric vehicles",
        )

        self.assertEqual(
            str(term),
            "Electric Vehicles (Electric mobility)",
        )


class ContextSeedRelationshipServiceTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password = "testpass123"
        )
        self.pearl_a = Pearl.objects.create(
            owner=self.user,
            source_type="url",
            original_value="https://example.com/a",
        )
        self.pearl_b =Pearl.objects.create(
            owner=self.user,
            source_type="url",
            original_value="https://example.com/b",
        )
        self.seed_a = ContextSeed.objects.create(
            pearl=self.pearl_a,
            seed_type="topic",
            value="electric vehicles",
        )
        self.seed_b = ContextSeed.objects.create(
            pearl=self.pearl_b,
            seed_type="topic",
            value="electric vehicles",
        )

    def test_persists_relationship_candidate(self):
        candidate = ContextSeedRelationshipCandidate(
            seed_a= self.seed_a,
            seed_b= self.seed_b,
            relationship_type=ContextSeedRelationshipType.SAME_VALUE
        )
        relationship = ContextSeedRelationshipService.create_relationship(
            candidate=candidate
        )

        self.assertEqual(ContextSeedRelationship.objects.count(), 1)
        self.assertEqual(relationship.relationship_type, ContextSeedRelationshipType.SAME_VALUE)

    def test_canonicalizes_seed_order(self):
        candidate = ContextSeedRelationshipCandidate(
            seed_a= self.seed_a,
            seed_b= self.seed_b,
            relationship_type= ContextSeedRelationshipType.SAME_VALUE
        )
        relationship = ContextSeedRelationshipService.create_relationship(
            candidate=candidate
        )
        self.assertLess(relationship.seed_a.pk, relationship.seed_b.pk)

    def test_does_not_create_duplicate_relationship(self):
        candidate =ContextSeedRelationshipCandidate(
            seed_a=self.seed_a,
            seed_b=self.seed_b,
            relationship_type=ContextSeedRelationshipType.SAME_VALUE
        )
        ContextSeedRelationshipService.create_relationship(
            candidate=candidate
        )
        ContextSeedRelationshipService.create_relationship(
            candidate=candidate
        )
        self.assertEqual(ContextSeedRelationship.objects.count(), 1)

    def test_does_not_allow_self_relationship(self):
        candidate = ContextSeedRelationshipCandidate(
            seed_a=self.seed_a,
            seed_b = self.seed_a,
            relationship_type=ContextSeedRelationshipType.SAME_VALUE
        )

        with self.assertRaises(ValueError):
            ContextSeedRelationshipService.create_relationship(
                candidate=candidate
            )

class ContextSeedRelationshipGenerationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password = "testpass123"
        )
        self.pearl_a = Pearl.objects.create(
            owner=self.user,
            source_type="url",
            original_value="https://example.com/a",
        )

        self.pearl_b = Pearl.objects.create(
            owner=self.user,
            source_type="url",
            original_value="https://example.com/b",
        )

        self.seed_a = ContextSeed.objects.create(
            pearl=self.pearl_a,
            seed_type="topic",
            value="electric vehicles",
        )

        self.seed_b = ContextSeed.objects.create(
            pearl=self.pearl_b,
            seed_type="topic",
            value="electric vehicles",
        )


    def test_generates_candidate_for_same_value(self):
        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b= self.seed_b
        )
        self.assertIsInstance(
            candidate,
            ContextSeedRelationshipCandidate
        )
        self.assertEqual(candidate.seed_a, self.seed_a)
        self.assertEqual(candidate.seed_b, self.seed_b)
        self.assertEqual(candidate.relationship_type, ContextSeedRelationshipType.SAME_VALUE)

    def test_returns_none_for_different_values(self):
        self.seed_b.value = "battery technology"
        self.seed_b.save()

        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b= self.seed_b
        )
        self.assertIsNone(candidate)

    def test_normalizes_seed_values_before_comparing(self):
        self.seed_a.value = " ELECTRIC VEHICLES "
        self.seed_a.save()

        self.seed_b.value = "Electric Vehicles"
        self.seed_b.save()

        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a= self.seed_a,
            seed_b= self.seed_b
        )

        self.assertIsNotNone(candidate)

    def test_does_not_relate_seed_from_same_pearl(self):
        seed_c = ContextSeed.objects.create(
            pearl = self.pearl_a,
            seed_type = "topic",
            value = "electric vehicle"
        )
        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a= self.seed_a,
            seed_b =seed_c
        )

        self.assertIsNone(candidate)

    def test_does_not_persist_relationship(self):
        ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b= self.seed_b
        )

        self.assertEqual(ContextSeedRelationship.objects.count(), 0)

    def test_discovers_conceptual_group_relationship(self):
        self.seed_a.value = "Electric Cars"
        self.seed_a.save()

        self.seed_b.value = "EVs"
        self.seed_b.save()

        group = ConceptualGroup.objects.create(
            name = "Electric Vehicles"
        )

        ConceptualGroupTerm.objects.create(
            group=group,
            value = "Electric Cars",
            normalized_value = "electric cars"
        )

        ConceptualGroupTerm.objects.create(
            group=group,
            value = "EVs",
            normalized_value = "evs"
        )

        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b=self.seed_b
        )

        self.assertIsNotNone(candidate)
        self.assertEqual(
            candidate.relationship_type,
            ContextSeedRelationshipType.CONCEPTUAL_GROUP
        )
    def test_does_not_discover_unrelated_conceptual_groups(self):
        self.seed_a.value = "Electric Cars"
        self.seed_a.save()

        self.seed_b.value = "Real Estate"
        self.seed_b.save()

        electric_group = ConceptualGroup.objects.create(
            name="Electric Vehicles",
        )

        property_group = ConceptualGroup.objects.create(
            name="Real Estate",
        )

        ConceptualGroupTerm.objects.create(
            group=electric_group,
            value="Electric Cars",
            normalized_value="electric cars",
        )

        ConceptualGroupTerm.objects.create(
            group=property_group,
            value="Real Estate",
            normalized_value="real estate",
        )

        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b=self.seed_b,
        )

        self.assertIsNone(candidate)

    def test_identical_normalized_values_use_same_value_type(self):
        self.seed_a.value = "Electric Vehicles"
        self.seed_a.save()

        self.seed_b.value = " electric vehicles "
        self.seed_b.save()

        candidate = ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b=self.seed_b,
        )

        self.assertIsNotNone(candidate)
        self.assertEqual(
            candidate.relationship_type,
            ContextSeedRelationshipType.SAME_VALUE,
        )

    def test_discovery_does_not_persist_relationship(self):
        self.seed_a.value = "Electric Cars"
        self.seed_a.save()

        self.seed_b.value = "EVs"
        self.seed_b.save()

        group = ConceptualGroup.objects.create(
            name="Electric Vehicles",
        )

        ConceptualGroupTerm.objects.create(
            group=group,
            value="Electric Cars",
            normalized_value="electric cars",
        )

        ConceptualGroupTerm.objects.create(
            group=group,
            value="EVs",
            normalized_value="evs",
        )

        initial_count = ContextSeedRelationship.objects.count()

        ContextSeedRelationshipGenerator.discover(
            seed_a=self.seed_a,
            seed_b=self.seed_b,
        )

        self.assertEqual(
            ContextSeedRelationship.objects.count(),
            initial_count,
        )

class ContextSeedRelationshipTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password="testpass123"
        )
        self.pearl_a = Pearl.objects.create(
            owner =self.user,
            source_type = "url",
            original_value = "https://example.com/a",
        )
        self.pearl_b = Pearl.objects.create(
            owner=self.user,
            source_type="url",
            original_value="https://example.com/b",
        )
        self.seed_a = ContextSeed.objects.create(
            pearl = self.pearl_a,
            seed_type ="topic",
            value="electric vehicles"
        )
        self.seed_b = ContextSeed.objects.create(
            pearl = self.pearl_b,
            seed_type = "concept",
            value ="battery technology"
        )

    def test_a_valid_relationship_can_be_created_between_two_seeds(self):
        relationship = ContextSeedRelationship.objects.create(
            seed_a = self.seed_a,
            seed_b = self.seed_b,
            relationship_type =ContextSeedRelationshipType.CONCEPTUAL_GROUP
        )

        self.assertEqual(relationship.seed_a, self.seed_a)
        self.assertEqual(relationship.seed_b, self.seed_b)
        self.assertEqual(
            relationship.relationship_type,
            ContextSeedRelationshipType.CONCEPTUAL_GROUP,
        )
    def test_seed_cannot_have_relationship_with_itself(self):
        with self.assertRaises(IntegrityError):
            ContextSeedRelationship.objects.create(
                seed_a = self.seed_a,
                seed_b = self.seed_a,
                relationship_type = ContextSeedRelationshipType.SAME_VALUE
            )
    def test_same_seed_pair_cannot_have_duplicate_relationship(self):
        ContextSeedRelationship.objects.create(
            seed_a = self.seed_a,
            seed_b =self.seed_b,
            relationship_type = ContextSeedRelationshipType.CONCEPTUAL_GROUP
        )
        with self.assertRaises(IntegrityError):
            ContextSeedRelationship.objects.create(
                seed_a = self.seed_a,
                seed_b =self.seed_b,
                relationship_type = ContextSeedRelationshipType.CONCEPTUAL_GROUP                
            )
    def test_relationship_preserves_seed_provenance(self):
        relationship = ContextSeedRelationship.objects.create(
            seed_a = self.seed_a,
            seed_b = self.seed_b,
            relationship_type = ContextSeedRelationshipType.CONCEPTUAL_GROUP
        )
        self.assertEqual(relationship.seed_a.pearl, self.pearl_a)
        self.assertEqual(relationship.seed_b.pearl, self.pearl_b)

class ContextSeedGeneratorServiceTest(TestCase):
    def setUp(self):
            self.user = get_user_model().objects.create(
                username="testuser",
                password="testpass123"
            )
            self.pearl = Pearl.objects.create(
                owner = self.user,
                source_type = "url",
                original_value = "https://example.com" \
                ""
            )
    def test_generated_candidates_are_persisted_as_context_seeds(self):
        
        metadata = {
            "title": "Introduction to Electric Vehicles",
            "description": "Learn how electric vehicle batteries work"
        }
        seeds  = ContextSeedGenerationService.generate_and_persist(
            pearl = self.pearl,
            metadata = metadata
        )
        self.assertEqual(len(seeds), 1)
        self.assertEqual(ContextSeed.objects.count(), 1)

        seed = seeds[0]

        self.assertEqual(self.pearl, seed.pearl)
        self.assertEqual(seed.seed_type, "topic")
        self.assertEqual(seed.value, "electric vehicles")

    def test_no_candidates_creates_no_context_seeds(self):
        metadata = {
            "title": "",
            "description": "",
        }

        seeds = ContextSeedGenerationService.generate_and_persist(
            pearl=self.pearl,
            metadata=metadata,
        )

        self.assertEqual(seeds, [])
        self.assertEqual(ContextSeed.objects.count(), 0)

    def test_context_can_be_created(self):
        context= Context.objects.create(
            owner = self.user,
            title = "ON REAL ESTATE DEVELOPMENT"
        )

        self.assertEqual(context.owner, self.user)
        self.assertEqual(context.title, "ON REAL ESTATE DEVELOPMENT")

    def test_pearl_can_belong_to_a_context(self):
        context = Context.objects.create(
            owner = self.user,
            title = "ON REAL ESTATE DEVELOPMENT"
        )
        relationship = ContextPearl.objects.create(
            context= context,
            pearl = self.pearl,
            source = ContextPearlSource.SYSTEM
        )

        self.assertEqual(relationship.context, context)
        self.assertEqual(relationship.pearl, self.pearl)

    def test_pearl_can_belong_to_multiple_contexts(self):
        context_one = Context.objects.create(
            owner = self.user,
            title = "ON REAL ESTATE DEVELOPMENT"
        )
        context_two = Context.objects.create(
            owner = self.user,
            title = "ON BUSINESS FINANCE"
        )

        ContextPearl.objects.create(
            context=context_one,
            pearl = self.pearl, 
            source = ContextPearlSource.SYSTEM
        )
        ContextPearl.objects.create(
            context=context_two,
            pearl = self.pearl,
            source = ContextPearlSource.USER
        )
        self.assertEqual(
            ContextPearl.objects.filter(
                pearl = self.pearl
            ).count(),
            2 
        )

    def test_context_pearl_records_source(self):
        context = Context.objects.create(
            owner = self.user,
            title = "ON REAL ESTATE DEVELOPMENT"
        )
        relationship = ContextPearl.objects.create(
            context=context,
            pearl= self.pearl,
            source= ContextPearlSource.USER
        )
        self.assertEqual(
            relationship.source, ContextPearlSource.USER
        )

    def test_same_pearl_cannot_be_added_to_same_context_twice(self):
        context = Context.objects.create(
            owner = self.user,
            title= "ON FOOTBALL CLUB OWNERSHIP"
        )
        ContextPearl.objects.create(
            context=context,
            pearl = self.pearl,
            source = ContextPearlSource.SYSTEM
        )

        with self.assertRaises(Exception):
            ContextPearl.objects.create(
                context=context,
                pearl = self.pearl,
                source=ContextPearlSource.USER
            )

class ContextSeedGeneratorTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser",
            password="testpass123"
        )
        self.pearl = Pearl.objects.create(
            owner = self.user,
            source_type = "url",
            original_value = "https://example.com" \
            ""
        )
    def test_generates_topic_seed_from_metadata(self):
        metadata = {
            "title": "Introduction to Electric Vehicles",
            "description": "Learn how electric vehicle batteries work"
        }

        candidates = ContextSeedGenerator.generate(
            pearl=self.pearl,
            metadata=metadata
        )

        self.assertTrue(
            any(
                isinstance(candidate, ContextSeedCandidate)
                and candidate.seed_type == "topic"
                and candidate.value == "electric vehicles"
                for candidate in candidates
            )
        )
    def test_can_generate_zero_candidates_when_evidence_is_insufficient(self):
        metadata= {
            "title": "",
            "description": ""
        }
        candidates = ContextSeedGenerator.generate(
            pearl= self.pearl,
            metadata= metadata
        )

        self.assertEqual(candidates, [])



    def test_does_not_generate_user_level_inference(self):
        metadata = {
            "title": "Introduction to Electric Vehicles",
            "description": "Learn how electric vehicle atteries work"            
        }
        candidates = ContextSeedGenerator.generate(
            pearl = self.pearl,
            metadata = metadata
        )
        wrong_inferences = [
                    "interest",
                    "goal",
                    "preference",
                    "belief",
                    "personality",                     
                 ]
        self.assertFalse(
             any(
                 candidate.seed_type in wrong_inferences
                 for candidate in candidates
             )
        )

    def test_generator_does_not_persist_candidates(self):
        metadata = {
            "title": "Introduction to Electric Vehicles",
            "description": "Learn how electric vehicle atteries work"              
        }
        candidates = ContextSeedGenerator.generate(
            pearl=self.pearl,
            metadata = metadata
        )
        self.assertEqual(ContextSeed.objects.count(), 0)

class ContextSeedTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser",
            password = "testpass123"
        )
        self.pearl = Pearl.objects.create(
            owner = self.user,
            source_type = "url",
            original_value="https://example.com",
        )

    def test_create_context_seed(self):
        context_seed = ContextSeed.objects.create(
            pearl = self.pearl,
            seed_type = "topic",
            value="electric vehicles",
            confidence = 0.97

        )
        self.assertEqual(context_seed.pearl, self.pearl)
        self.assertEqual(context_seed.seed_type, "topic")
        self.assertEqual(context_seed.value, "electric vehicles")
        self.assertEqual(context_seed.confidence, 0.97)
    def test_contextseed_is_attached_to_valid_pearl(self):
        pass


class ContextSeedServiceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser",
            password = "testpass123"
        )
        self.pearl = Pearl.objects.create(
            owner = self.user,
            source_type = "url",
            original_value="https://example.com",            
        )
    def test_service_creates_context_seed(self):
        context_seed = ContextSeedService.create_seed(
            pearl = self.pearl,
            seed_type = "topic",
            value="electric vehicles",
            confidence = 0.97            
        )
        self.assertEqual(context_seed.pearl, self.pearl)
        self.assertEqual(context_seed.seed_type, "topic")
        self.assertEqual(context_seed.value, "electric vehicles")
        self.assertEqual(context_seed.confidence, 0.97)
    def test_no_pearl_raises_error(self):
           
        with self.assertRaises(ValueError) :
            ContextSeedService.create_seed(
                pearl = None,
                seed_type = "topic",
                value="electric vehicles",
                confidence = 0.97            
            ) 
            print("Context seed creation requires Pearl")

    def test_no_value_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            ContextSeedService.create_seed(
                pearl = self.pearl,
                seed_type = "topic",
                value= None,
                confidence = 0.97            
            ) 
        exception = cm.exception
        print(type(exception))
        
        # self.assertEqual(exception, "Seed Value is required")