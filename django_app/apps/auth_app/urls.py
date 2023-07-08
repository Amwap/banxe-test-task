from django.urls import path
from apps.auth_app.views import register
# Create your tests here.

urlpatterns = [
    path('register/', register, name='register'),
]