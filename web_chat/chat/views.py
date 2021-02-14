import json

from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .forms import UsersFormRegister, SearchUsers
from django.contrib.auth.views import LoginView, LogoutView


def chat(request, room_name):
    return render(request, 'chat.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def index(request):
    if request.method == 'GET':
        form = SearchUsers(request.GET)
        search_query = request.GET.get('query', '')
        if User.objects.filter(username=search_query).exists():
            return redirect('chat')
        else:
            messages.error(request, 'Нет такого пользователя')
    else:
        form = SearchUsers()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UsersFormRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')
        else:
            error = 'Ошибка в имени или пароле. Попробуйте изменить имя и/или пароль'
            print(form.error_messages)
    else:
        form = UsersFormRegister()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'reg.html', context)


def start_chat(request):
    return render(request, 'start_chat.html')


class MyLoginView(LoginView):
    template_name = 'auth.html'


class MyLogoutView(LogoutView):
    next_page = '/'
