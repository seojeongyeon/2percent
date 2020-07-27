from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('user_list/<int:user_id>', views.user_list, name="user"),
    path('mypage/', views.mypage, name="mypage"),
    path('follow/<int:user_id>', views.follow, name="follow"),
]