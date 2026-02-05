from os import name
from pyexpat import model
from time import time
from typing import Type
from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
import time
import datetime

# Create your models here.

class User(AbstractUser):
    """Custom User model extending Django's AbstractUser"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Override groups and user_permissions to avoid reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """Extended user profile with additional information"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_links = models.JSONField(default=dict, blank=True)
    preferences = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s profile"


CONTENT_TYPE_CHOICES = [
    ('article', 'Article'),
    ('video', 'Video'),
    ('image', 'Image'),
    ('note', 'Note'),
    ('audio', 'Audio'),
    ('link', 'Link'),
    ('document', 'Document'),
]


class Tag(models.Model):
    """Tag model for categorizing pearls"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=20, choices=[('auto', 'Auto-generated'), ('user', 'User-created')], default='user')
    usage_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-usage_count', 'name']

    def __str__(self):
        return self.name


class Folder(models.Model):
    """Folder model for organizing pearls"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    is_auto_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['user', 'name', 'parent']

    def __str__(self):
        return self.name


class Post(models.Model):
    """Pearl (Post) model - the core content entity"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pearls')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='note')
    url = models.URLField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    tags = models.ManyToManyField(Tag, related_name='pearls', blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, related_name='pearls')
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Legacy fields for backward compatibility (will be migrated)
    pearl_category = models.CharField(max_length=200, blank=True, null=True)
    pearl_image = models.FileField(upload_to="media/img", blank=True, null=True)
    pearl_audio = models.FileField(upload_to="media/audio", blank=True, null=True)
    pearl_video = models.FileField(upload_to="media/video", blank=True, null=True)
    pearl_scripture = models.CharField(max_length=200, blank=True, null=True)
    pearl_summary = models.CharField(max_length=200, blank=True, null=True)
    # archived = models.ManyToManyField('User', related_name='archived_pearls', blank=True)  # Temporarily removed

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['is_public', '-created_at']),
            models.Index(fields=['content_type']),
        ]

    def __str__(self):
        return self.title or f"Pearl {self.id}"

    def get_absolute_url(self):
        return reverse('pearl_detail', args=[str(self.id)])


# Legacy model for backward compatibility
TITLE_CHOICES = [
    ("FOR FAITH", "for faith"),
    ('FOR WISDOM', "for wisdom"),
    ('FOR LOVE', "for love"),
    ('FOR POWER', "for power"),
    ("FOR STRENGTH", "for strength"),
    ('FOR RICHES', "for riches"),
    ('FOR HONOUR', "for honour"),
    ('FOR BLESSING', "for blessing"),
    ('FOR GLORY', "for glory"),
]
#
#     # text = models.ForeignKey(Post.text, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.category
#
#     def get_absolute_url(self):
#         return reverse('pearl_detail', args=[str(self.id)])