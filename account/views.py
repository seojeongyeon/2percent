from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from .forms import LoginForm, RegisterForm

User = get_user_model()

# Create your views here.
def signin(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request)
        if form.is_valid():
            nickname = form.cleaned_data.get("nickname")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, nickname=nickname, password=password)
    else:
        form = LoginForm()
        return render(request, "signin.html", {"form":form})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, "signup.html", {"form":form})
    else:

        form = RegisterForm()
        return render(request, "signup.html", {"form":form})

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
    return render(request, 'user_list.html', { 'user': user })