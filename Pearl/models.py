from django.db import models
from django.urls import reverse
from .forms import User
from django.utils import timezone
import datetime
# Create your models here.


class Post(models.Model):
    category = models.CharField(max_length=200)
    pearl = models.FileField(upload_to="media/img")
    text = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    archived = models.ManyToManyField(User, related_name='archived_by', blank=True)

    def __str__(self):
        return self.category

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