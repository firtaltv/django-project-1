from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'input-group-append',
                'placeholder': 'Username'
            }),
            'email': TextInput(attrs={
                'class': 'input-group-append',
                'placeholder': 'E-Mail'
            }),
            'password1': PasswordInput(attrs={
                'class': 'input-group-append',
                'placeholder': 'Password'
            }),
            'password2': PasswordInput(attrs={
                'class': 'input-group-append',
                'placeholder': 'Re-enter Password'
            }),
        }