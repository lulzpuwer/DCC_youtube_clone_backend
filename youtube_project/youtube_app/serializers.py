from rest_framework import serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']
       

class ReplySerializer(serializers.ModelSerializer):
  class Meta:
    model = Reply
    fields = ['id','user', 'comment', 'text','user_id', 'commentt_id']
    depth = 1
  comment_id = serializers.IntegerField(write_only = True)
