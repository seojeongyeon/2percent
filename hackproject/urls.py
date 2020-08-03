"""hackproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from two import views
import account.urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('photoshop/', views.photoshop, name='photoshop'),
    path('photodetail/<int:pk>', views.photodetail, name='photodetail'),
    path('photodetail/<int:pk>/photoscrap', views.photoscrap, name='photoscrap'),
    path('photodetail/<int:pk>/photoscrap_del', views.photoscrap_del, name='photoscrap_del'),
    path('contest/', views.contest, name='contest'),
    path('mission/', views.mission, name='mission'),
    path('account/', include(account.urls)),
    path('comment_delete/<int:comment_id>', views.comment_delete, name="comment_delete"),
    path('mission_detail/<int:mission_id>', views.mission_detail, name='mission_detail'),
    path('mission_detail/<int:mission_id>/mission_scrap', views.mission_scrap, name='mission_scrap'),
    path('mission_detail/<int:mission_id>/mission_scrap_del', views.mission_scrap_del, name='mission_scrap_del'),
    path('mission_create/', views.mission_create, name='mission_create'),
    path('mission_delete/<int:mission_id>', views.mission_delete, name='mission_delete'),
    path('mission_comment_create/<int:mission_id>', views.mission_comment_create, name='mission_comment_create'),
    path('mission_comment_delete/<int:comment_id>', views.mission_comment_delete, name='mission_comment_delete'),
    path('commenting/<int:pk>', views.commenting, name= 'commenting'),
    path('comment_like/<int:pk>', views.comment_like, name='like'),
    path('mission_comment_like/<int:comment_id>', views.mission_comment_like, name='mission_comment_like'),
    path('photowrite/', views.photowrite, name='photowrite'),
    path('photo_search/', views.photo_search, name='photo_search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

