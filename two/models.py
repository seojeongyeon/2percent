from django.db import models
from django.conf.auth.models import User
from django.conf import settings
from pytz import timezone

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


class Photoshop(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    device_CHOICES = (('핸드폰', 'phone'), ('카메라', 'camera'),('필름카메라','filmcamera'))
    device = models.CharField(max_length=7, choices=device_CHOICES)
    color_CHOICES = (('비비드한', 'vivid'), ('모노톤', 'mono'), ('빈티지한','Vintage'))
    color = models.CharField(max_length=8, choices=color_CHOICES)
    kind_CHOICES =(('셀카', 'selfic'), ('풍경', 'scenery'), ('음식','food'),('코디', 'style'))
    kind= models.CharField(max_length=7,choices=kind_CHOICES)
    method_CHOICES =(('어플', 'apps'), ('기본카메라', 'basic'))
    method =models.CharField(max_length=8,choices=method_CHOICES)
    fix_CHOICES = (('얼굴', 'face'), ('색감', 'color'))
    fix = models.CharField(max_length=8,choices=fix_CHOICES)
    app = models.CharField(max_length=10)
    photobefore = models.ImageField(upload_to="image/")
    photoafter = models.ImageField(upload_to="image/")
    explain = models.TextField()
