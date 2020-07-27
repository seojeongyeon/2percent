from django.db import models
from django.conf import settings
from pytz import timezone

# Create your models here.
class Photoshop(models.Model):
    title = models.CharField(max_length=70, null=True)
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

    def __str__(self):
        return self.title

class Comment(models.Model):
    photoshop = models.ForeignKey(Photoshop, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    body = models.TextField()
    pub_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.author}님이 {self.photoshop}에 단 댓글"

class ask(models.Model):
    title = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="ask/profile_pic")
    photo = models.ImageField(blank=True, upload_to="ask")
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

class Mission(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=2)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    point = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    
class MissionComment(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    writer = models.CharField(max_length=2)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    isPicked = models.BooleanField(default=False)

    def getlikes(self) :
        return len(self.likers.all())

