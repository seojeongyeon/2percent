from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from hackproject import settings

User = get_user_model()

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = User
        fields = ['username', "nickname", "profile", "email", "info", "password1", "password2", "birthday"]

class UserEditForm(UserChangeForm):
    birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = User
        fields = ['profile', 'nickname', 'info', 'birthday' ]