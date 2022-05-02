from . import views
from django.urls import path


urlpatterns = [
    path('', views.videos),
    path('<int:pk>', views.video_comments),
]