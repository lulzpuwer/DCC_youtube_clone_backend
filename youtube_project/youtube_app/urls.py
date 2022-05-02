from . import views
from django.urls import path


urlpatterns = [
    path('', views.user_comments),
    path('all/', views.get_all_comments),
]