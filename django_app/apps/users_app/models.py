from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.auth_app.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Auth model """
    username = models.CharField(_('Username'), max_length=255, unique=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    is_active = models.BooleanField(_('Active'), default=False)
    is_staff = models.BooleanField(_('Is stuff'), default=False)
    is_verified = models.BooleanField(_('Verified'), default=False)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"{self.email}"
