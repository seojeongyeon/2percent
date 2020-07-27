from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from hackproject import settings

User = get_user_model()

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = User
        fields = ['username', "nickname", "password1", "password2", "profile"]

class UserEditForm(UserChangeForm):
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        # 어떤 모델을 기반으로 입력 받을 건지
        model = User
        # 원하는 값, 다른 곳에서 처리하려면 view에서 처리...
        fields = ['profile', 'nickname' ]
