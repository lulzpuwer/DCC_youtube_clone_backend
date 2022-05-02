from django.db import models

# Create your models here.

class Comment(models.model):
  user = models.ForeignKey
  video_id = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  likes = models.IntegerField()
  dislikes = models.IntegerField()

class Reply(models.model):
  user = models.ForeignKey
  comment = models.ForeignKey
  text = models.CharField(max_length=255)