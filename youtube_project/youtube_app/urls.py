from . import views
from django.urls import path


urlpatterns = [
    path('comment/<slug:video>', views.user_comments),
    path('all/', views.get_all_comments),
]