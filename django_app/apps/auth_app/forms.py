from django import forms
from apps.users_app.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = []

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']