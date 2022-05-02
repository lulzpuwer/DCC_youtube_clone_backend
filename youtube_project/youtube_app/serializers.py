from rest_framework import serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'video_id', 'text', 'likes', 'dislikes']
        depth = 1

class ReplySerializer(serializers.ModelSerializer):
  class Meta:
    model = Reply
    fields = ['user', 'comment', 'text']
    depth = 1
