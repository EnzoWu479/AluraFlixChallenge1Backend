from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    name=models.CharField(max_length=255, default="")
    password=models.CharField(max_length=255, default="")
    email=models.CharField(max_length=255, unique=True, default="")
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]
    