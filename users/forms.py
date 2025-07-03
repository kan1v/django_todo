from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Ваш логин или Email: ', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Пароль: ', strip=False, widget=forms.PasswordInput)