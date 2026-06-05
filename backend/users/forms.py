from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'avatar',
            'phone',
            'bio',
        ]

        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
        }


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )