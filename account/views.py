from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout, update_session_auth_hash
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserEditForm
from django.core.paginator import Paginator

# 이메일 인증을 위한 import
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

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
            # 이메일 중복 검사
            # if User.objects.filter(email=form.cleaned_data.get('email')).exists():
            #     return HttpResponse('이미 사용 중인 이메일입니다')
            user = form.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request) 
            # localhost:8000
            message = render_to_string('activate.html',                         {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = "[2%를 부탁해] 회원가입 인증 메일입니다."
            user_email = user.email
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                '</div>'
            )
            return redirect('home')
        return render(request, "signup.html", {"form":form})
    else:
        form = RegisterForm()
        return render(request, "signup.html", {"form":form})

def signout(request):
    logout(request)
    return redirect('home')


# 마이페이지 노출
def mypage(request):
    if not request.user: return redirect('signin')
    d_user = request.user
    # photoshop scraps paginator
    photoshops = d_user.pscraps.all()
    p_paginator = Paginator(photoshops, 4)
    ppage = request.GET.get('page')
    photoscraps = p_paginator.get_page(ppage)
    # mission scraps paginator
    missions = d_user.mscraps.all()
    m_paginator = Paginator(missions, 4)
    mpage = request.GET.get('page')
    missionscraps = m_paginator.get_page(mpage)
    return render(request, 'mypage.html',{ 'd_user': d_user, 'photoscraps': photoscraps, 'missionscraps': missionscraps })

# 유저 페이지 노출
def user(request, username):
    d_user = get_object_or_404(User, username=username)
    # photoshop paginator
    photoshops = d_user.photoshop.all()
    p_paginator = Paginator(photoshops, 8)
    ppage = request.GET.get('page')
    photocut = p_paginator.get_page(ppage)
    # mission paginator
    missions = d_user.mission.all()
    m_paginator = Paginator(missions, 8)
    mpage = request.GET.get('page')
    missioncut = m_paginator.get_page(mpage)
    # mission comment paginator
    mission_comments = d_user.missionwriter.all()
    mc_paginator = Paginator(mission_comments, 8)
    mcpage = request.GET.get('page')
    commentcut = mc_paginator.get_page(mcpage)
    return render(request, 'user.html',{ 'd_user': d_user, 'photocut':photocut, 'missioncut': missioncut, 'commentcut': commentcut})

# 팔로잉 리스트 노출
def following(request, username):
    user = get_object_or_404(User, username=username)
    flist = user.followings.all()
    paginator = Paginator(flist, 5)
    page = request.GET.get('page')
    fusers = paginator.get_page(page)
    return render(request, 'flist.html', { 'fusers': fusers })

# 팔로워 리스트 노출
def follower(request, username):
    user = get_object_or_404(User, username=username)
    flist = user.followers.all()
    paginator = Paginator(flist, 5)
    page = request.GET.get('page')
    fusers = paginator.get_page(page)
    return render(request, 'flist.html', { 'fusers': fusers })

# 유저 팔로우 기능
def follow(request, username):
    # request.user -> user(username=username) 팔로우(request.user following 리스트에 user를 추가)
    user = get_object_or_404(User, username=username)
    if request.user != user:
        user.followers.add(request.user)
        user.save()
    return redirect('user', username=username)

# 유저 언팔 기능
def unfollow(request, username):
    # request.user -> user(username=usernam) 팔로우(request.user following 리스트에 user를 추가)
    user = get_object_or_404(User, username=username)
    if request.user != user:
        user.followers.remove(request.user)
        user.save()
    return redirect('user', username=username)

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


### 이메일 인증을 통한 유저 활성화 기능
def activate(request, uid64, token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('비정상적인 접근입니다.')