from django.urls import path
from apps.auth_app.views import register, login_view
# Create your tests here.

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]