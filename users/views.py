from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')

# def register(request):
#     '''register new user'''
#     if request.method != 'POST':
#         # Выводит пустую форму регистрации
#         form = UserCreationForm()
#     else:
#         # Обработка заполненной формы
#         form = UserCreationForm(data=request.POST)
#
#         if form.is_valid():
#             new_user = form.save()
#             # Вход и перенаправление на домашнюю страницу
#             login(request, new_user)
#             return redirect('souvenirs_app:index')
#
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
    # return redirect('souvenirs_app:index')
    # return HttpResponseRedirect('/')