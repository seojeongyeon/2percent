from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('user/<int:user_id>', views.user, name="user"),
    path('mypage/', views.mypage, name="mypage"),
    path('follower/<int:user_id>', views.follower, name="follower"),
    path('following/<int:user_id>', views.following, name="following"),
    path('follow/<int:user_id>', views.follow, name="follow"),
    path('unfollow/<int:user_id>', views.unfollow, name="unfollow"),
    path('info_setting/', views.info_setting, name="info_setting"),
    path('pw_setting/', views.pw_setting, name="pw_setting"),
]