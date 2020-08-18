from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Photoshop(models.Model):
    title = models.CharField(max_length=70, null=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="photoshop")
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
    explain = models.TextField(help_text='사진에 적용된 보정법들을 모두 써주세요!')
    photo_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='photo_like')

    def __str__(self):
        return self.title

    def getlike(self):
        return len(self.photo_like.all())

    def summary(self): 
        return self.explain[:100]


class Comment(models.Model):
    photoshop = models.ForeignKey(Photoshop, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    body = models.TextField()
    pub_date = models.DateField(auto_now_add = True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')
    
    def __str__(self):
        return f"{self.author}님이 {self.photoshop}에 단 댓글"

    def getlike(self):
        return len(self.like.all())


class Mission(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mission")
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    point = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    pick = models.IntegerField(default=None, blank=True, null=True)

    def end(self):
        return self.end_date < timezone.now()
    

            
class MissionComment(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="missionwriter")
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="missionlikers")
    isPicked = models.BooleanField(default=False)

    def getlikes(self) :
        return len(self.likers.all())

class Contest(models.Model):
    # image = models.ImageField(upload_to="image")
    image = ProcessedImageField(
               upload_to='contest_image_path', # 저장 위치
               processors=[ResizeToFill(600,600)], # 처리할 작업 목록
               format='JPEG', # 저장 포맷(확장자)
               options= {'quality': 90 }, # 저장 포맷 관련 옵션 (JPEG 압축률 설정)
        )
    contest_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contest_like')

    def getlike(self):
        return len(self.like.all())

    #이미지 크기 수정
    def contest_image_path(instance, filename): 
        return f'contests/{instance.contest}/{instance.contest}.jpg'


