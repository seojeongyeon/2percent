from django.db import models
from django.conf.auth.models import User

# Create your models here.

class Mission(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    point = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    
class MissionComment(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    isPicked = models.BooleanField()
