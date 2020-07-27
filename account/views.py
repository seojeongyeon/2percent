from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout, update_session_auth_hash
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserEditForm

User = get_user_model()

# Create your views here.
def signin(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, "signin.html", {"form":form})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, "signup.html", {"form":form})
    else:

        form = RegisterForm()
        return render(request, "signup.html", {"form":form})

def signout(request):
    logout(request)
    return redirect('home')



# 마이페이지 노출
def mypage(request):
    return render(request, 'mypage.html')

# 유저 페이지 노출
def user(request, user_id):
    d_user = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', { 'd_user': d_user })

# 팔로잉 리스트 노출
def following(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    fusers = user.followings.all()
    return render(request, 'flist.html', { 'fusers': fusers })

# 팔로워 리스트 노출
def follower(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    fusers = user.followers.all()
    return render(request, 'flist.html', { 'fusers': fusers })

# 유저 팔로우 기능
def follow(request, user_id):
    # request.user -> user(pk=user_id) 팔로우(request.user following 리스트에 user를 추가)
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:
        user.followers.add(request.user)
        user.save()
    return redirect('user', user_id)

# 유저 언팔 기능
def unfollow(request, user_id):
    # request.user -> user(pk=user_id) 팔로우(request.user following 리스트에 user를 추가)
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:
        user.followers.remove(request.user)
        user.save()
    return redirect('user', user_id)

def info_setting(request): 
    if request.method == "GET":
        form = UserEditForm(instance=request.user)
    else:
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mypage')
    return render(request, 'setting.html', { 'form': form })

def pw_setting(request):
    if request.method == "GET":
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('mypage')
    return render(request, 'setting.html', { 'form': form })
