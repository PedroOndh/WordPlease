from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

# Create your views here.
from django.views import View

from users.forms import loginForm, UserForm


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = loginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
        context = {'form': form}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        django_logout(request)
        return redirect('login')


class NewUserView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'users/new_user.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        context = {'form': form}
        return render(request, 'users/new_user.html', context)
