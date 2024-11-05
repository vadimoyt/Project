from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import CustomUser


class RegistrationForm(UserCreationForm):
    ROLE_CHOISES = [
        ('Buyer', 'Buyer'),
        ('owner', 'Owner')
    ]
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOISES, label='Роль')

    class Meta:
        model = CustomUser
        fields = ("username","email", "role", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

