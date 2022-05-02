from os import name
from pyexpat import model
from time import time
from typing import Type
from unicodedata import category
from django.db import models
from django.urls import reverse
from .forms import User
from django.utils import timezone
import time
import datetime
# Create your models here.


TITLE_CHOICES = [
    ("FOR FAITH", "for faith",),
    ('FOR WISDOM', "for wisdom"),
    ('FOR LOVE', "for love"),
    ('FOR POWER', "for power"),
    ("FOR STRENGTH", "for strength",),
    ('FOR RICHES', "for riches"),
    ('FOR HONOUR', "for honour"),
    ('FOR BLESSING', "for blessing"),
    ('FOR GLORY', "for glory"),
]

class Post(models.Model):
    pearl_category = models.CharField(max_length=200, choices=TITLE_CHOICES)
    pearl_image = models.FileField(upload_to="media/img")
    pearl_audio = models.FileField(upload_to="media/audio")
    pearl_video = models.FileField(upload_to="media/video")
    pearl_scripture = models.CharField(max_length=200)
    pearl_summary = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    # todays_date = models.TimeField(default= time.asctime(time.localtime(time.time())))
    archived = models.ManyToManyField(User, related_name='archived_by', blank=True)

    def __str__(self):
        return self.pearl_category

    def get_absolute_url(self):
        return reverse('pearl_detail', args=[str(self.id)])


# class Archive(models.Model):
#
#     # category = models.ForeignKey(Post.category, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     category = Post.category
#     pearl = Post.pearl
#
#     # text = models.ForeignKey(Post.text, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.category
#
#     def get_absolute_url(self):
#         return reverse('pearl_detail', args=[str(self.id)])