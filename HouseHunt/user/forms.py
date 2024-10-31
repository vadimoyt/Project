from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import CustomUser


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username","email", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

