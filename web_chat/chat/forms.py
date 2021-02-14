from django.forms import ModelForm, TextInput, PasswordInput, CharField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UsersFormRegister(UserCreationForm):
    email = CharField(max_length=40, required=False, help_text='Email (Опционально)')
    first_name = CharField(max_length=30, required=False, help_text='Имя (Опционально)')
    last_name = CharField(max_length=30, required=False, help_text='Фамилия (Опционально)')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UsersFormAuthentication(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(),
            'password': PasswordInput()
        }


class SearchUsers(ModelForm):
    query = CharField()

    class Meta:
        model = User
        fields = ['username']
