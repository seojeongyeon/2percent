from django.contrib import admin
from .models import Photoshop, Comment, Contest, Mission, MissionComment
# Register your models here.

admin.site.register(Photoshop)
admin.site.register(Comment)
admin.site.register(Mission)
admin.site.register(MissionComment)
admin.site.register(Contest)