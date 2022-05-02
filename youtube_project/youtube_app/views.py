from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializers

# Create your views here.


