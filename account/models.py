from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from account.managers import AccountManager
from account.choices import STATUS_CHOICES
from account.tasks import generate_token

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='User')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

# class Verification(models.Model):

#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     token = models.CharField(max_length=120, default=generate_token)
#     expire_date = models.BooleanField(default=False)
#     create_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.user} {self.token}"
