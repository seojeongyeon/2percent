from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('user/<slug:username>', views.user, name="user"),
    path('mypage/', views.mypage, name="mypage"),
    path('follower/<slug:username>', views.follower, name="follower"),
    path('following/<slug:username>', views.following, name="following"),
    path('follow/<slug:username>', views.follow, name="follow"),
    path('unfollow/<slug:username>', views.unfollow, name="unfollow"),
    path('info_setting/', views.info_setting, name="info_setting"),
    path('pw_setting/', views.pw_setting, name="pw_setting"),
]