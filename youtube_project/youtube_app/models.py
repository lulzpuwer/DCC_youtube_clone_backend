from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Comment

# Create your models here.

class Comment(models.model):
  user = models.ForeignKey(Comment, on_delete=models.CASCADE)
  video_id = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  likes = models.IntegerField()
  dislikes = models.IntegerField()

class Reply(models.model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)