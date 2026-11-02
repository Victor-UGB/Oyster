from django.db import models
import uuid
from django.conf import settings
from Pearl.models import Pearl

# Create your models here.



class ContextSeedRelationshipType(models.TextChoices):
    SAME_VALUE = "same_value", "Same Value"
    CONCEPTUAL_GROUP = "conceptual_group", "Conceptual Group"


class ContextSeed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pearl = models.ForeignKey(Pearl, on_delete=models.CASCADE, related_name="context_seeds")
    seed_type = models.CharField(max_length=40)
    value = models.CharField(max_length=240)
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.seed_type}: {self.value}"

    
class ContextSeedRelationship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seed_a = models.ForeignKey(ContextSeed, on_delete=models.CASCADE, related_name="relationships_as_a")
    seed_b = models.ForeignKey(ContextSeed, on_delete=models.CASCADE, related_name="relationships_as_b")
    relationship_type = models.CharField(max_length=24, choices=ContextSeedRelationshipType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(seed_a=models.F("seed_b")),
                name="prevent_self_relationship",
            ),
            models.UniqueConstraint(
                fields=["seed_a", "seed_b"],
                name="unique_seed_relationship"
            )
        ]

    def __str__(self):
        return f"{self.seed_a} <-> {self.seed_b}"


class Context(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contexts")
    title = models.CharField(max_length=244, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class ContextPearlSource(models.TextChoices):
    SYSTEM = "system", "System"
    USER = "user", "User"


class ContextPearl(models.Model):
    pearl = models.ForeignKey(Pearl, on_delete=models.CASCADE, related_name="context_relationships")
    context = models.ForeignKey(Context, on_delete=models.CASCADE, related_name="context_pearls")
    source = models.CharField(max_length=20, choices=ContextPearlSource.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["context", "pearl"], name="unique_context_pearl")
        ]

    def __str__(self):
        return f"{self.pearl} -> {self.context}"


class ConceptualGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f"{self.name}"


class ConceptualGroupTerm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(ConceptualGroup, on_delete=models.CASCADE, related_name="terms")
    value = models.CharField(max_length=200, blank=False)
    normalized_value = models.CharField(max_length=200, blank=False )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =["normalized_value"]
        constraints = [
            models.UniqueConstraint(
                fields=["group", "normalized_value"],
                name = "unique_normalized_ter_per_group",
            ),
        ]

    def __str__(self):
        return f'{self.value} ({self.group})'