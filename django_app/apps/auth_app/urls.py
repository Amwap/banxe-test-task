from django.urls import path
from apps.auth_app.views import register, login_view, logout_view
# Create your tests here.

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]