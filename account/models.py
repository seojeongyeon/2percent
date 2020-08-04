from django.db import models
from django.contrib.auth.models import AbstractUser
from hackproject import settings
from two.models import *

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='account/', blank=True, null=True)
    email = models.EmailField(max_length=200)
    info = models.TextField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    point = models.IntegerField(default=0)
    
    pscraps = models.ManyToManyField(Photoshop, related_name="pscrap_users")
    mscraps = models.ManyToManyField(Mission, related_name="mscrap_users")

    ## 이메일 인증 시 true 값
    is_active = models.BooleanField(default=False)

    class Meta(object):
        unique_together = ('email',)