from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_comments(request,video_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        comment = Comment.objects.filter(video_id=video_id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)



@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def get_all_replies(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        reply = Reply.objects.filter(user_id=request.user.id)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)



@api_view(['PUT', 'GET', 'POST'])
@permission_classes([IsAuthenticated])
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        reply = Reply.objects.filter(comment_id=pk)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        reply = get_object_or_404(Reply, comment_id=pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# Create your views here