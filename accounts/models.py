from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False, null=False)
    is_mentor = models.BooleanField(default=False, null=False)
    is_intern = models.BooleanField(default=False, null=False)
    status = models.BooleanField(default=False, null=False)
