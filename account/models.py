from django.db import models
from django.contrib.auth.models import AbstractUser
from hackproject import settings

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='account/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')