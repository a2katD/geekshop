from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfilerForm
from baskets.models import Basket

class Login(LoginView):
    authentication_form = UserLoginForm
    template_name = 'authapp/login.html'
    title = 'Geekshop | Авторизация'


class RegisterView(CreateView):
    form_class  = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    template_name = 'authapp/register.html'
    title = 'Geekshop | Регистрация'

class ProfileView(CreateView):
    form_class  = UserProfilerForm
    success_url = reverse_lazy('authapp:profile')
    template_name = 'authapp/profile.html'
    title = 'Geekshop | Профиль'

class Logout(LogoutView):
    form_class  = UserProfilerForm
    title = 'Geekshop | Профиль'

# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

