from django.urls import path
from apps.wallet_app.views import HomeView, cancel_transaction
# Create your tests here.

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('transaction/<int:pk>/cancel/', cancel_transaction, name='cancel_transaction'),
]