from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def signout(request):
    return render(request, 'signout.html')

def mypage(request):
    return render(request, 'mypage.html')

def user_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_list.html', { 'user': user })

def following(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    fusers = user.following.all()
    return render(request, 'follow.html', { 'fusers': fusers })

def follower(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    fusers = user.followers.all()
    return render(request, 'follow.html', { 'fusers': fusers })


def follow(request, user_id):
    # request.user -> user(pk=user_id) 팔로우(request.user following 리스트에 user를 추가)
    user = get_object_or_404(User, pk=user_id)
    user.followers.add(request.user)
    return redirect()