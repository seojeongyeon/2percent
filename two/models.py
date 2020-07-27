from django.db import models

# Create your models here.

class Comment(models.Model):
    photoshop = models.Foreignkey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models. Foreignkey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
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