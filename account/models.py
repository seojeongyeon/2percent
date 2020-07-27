from django.db import models
from django.contrib.auth.models import AbstractUser
from hackproject import settings

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField()
    profile = models.ImageField(upload_to='account/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)