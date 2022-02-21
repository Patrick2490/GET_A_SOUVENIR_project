from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class RegisterUser(CreateView):
    '''
    View for the registration 
    '''
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')

class LoginUser(LoginView):
    '''
    View for the login 
    '''
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

def logout_view(request):
    '''
    View for the logout 
    '''
    logout(request)
    return render(request, 'registration/logout.html')
    # return redirect('souvenirs_app:index')
    # return HttpResponseRedirect('/')