from django.contrib import messages
from django.contrib.auth import authenticate
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


def new_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                messages.success(request, 'Usuario creado correctamente con ID {0}'.format(new_user.pk))
                form = UserForm()
        else:
            form = UserForm()

        context = {'form': form}
        return render(request, 'users/new_user.html', context)
