from django.urls import path
from apps.wallet_app.views import HomeView
# Create your tests here.

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]