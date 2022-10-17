from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.fields.CharField(max_length=64)
    last_name = models.fields.CharField(max_length=64)
