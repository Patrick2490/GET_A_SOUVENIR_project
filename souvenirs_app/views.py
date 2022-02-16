from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.text import slugify

from django.contrib.auth.models import User
from .models import Souvenir, UserInfo, Country
from .forms import SouvenirForm, UserInfoForm

import random


def index(request):
    return render(request, 'souvenirs_app/index.html')


class SouvenirsView(ListView):
    model = Souvenir
    template_name = 'souvenirs_app/souvenirs.html'
    context_object_name = 'souvenirs'


class SouvenirView(DetailView):
    model = Souvenir
    # pk_url_kwarg = 'souvenir_id'
    slug_url_kwarg = 'souvenir_slug'
    context_object_name = 'souvenir'
    # souvenir = Souvenir.objects.get(souvenir_id=pk)
    template_name = 'souvenirs_app/souvenir.html'


class SendUserSouvenirsView(LoginRequiredMixin, ListView):
    model = Souvenir
    template_name = 'souvenirs_app/send_user_souvenirs.html'
    context_object_name = 'send_user_souvenirs'

    def get_queryset(self):
        return Souvenir.objects.filter(send_user__slug=self.request.user)


class ReceiveUserSouvenirsView(LoginRequiredMixin, ListView):
    model = Souvenir
    template_name = 'souvenirs_app/receive_user_souvenirs.html'
    context_object_name = 'receive_user_souvenirs'

    def get_queryset(self):
        return Souvenir.objects.filter(receive_user__slug=self.request.user)


class CreateSouvenir(LoginRequiredMixin, CreateView):
    model = Souvenir
    form_class = SouvenirForm
    template_name = 'souvenirs_app/create_souvenir.html'
    context_object_name = 'create_souvenir'

    def form_valid(self, form):
        form.instance.send_user = UserInfo.objects.get(username=self.request.user)
        form.instance.receive_user = random.choice(UserInfo.objects.exclude(username=self.request.user))
        print(form.instance.send_user, form.instance.receive_user)
        random_number = str(random.randint(0, 99999)).zfill(5)
        form.instance.slug = f'{UserInfo.objects.get(username=form.instance.send_user).country.code}' \
                             f'{random_number}' \
                             f'{UserInfo.objects.get(username=form.instance.receive_user).country.code}'
        return super(CreateSouvenir, self).form_valid(form)


class CreateUserInfo(LoginRequiredMixin, CreateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'souvenirs_app/create_user_info.html'
    context_object_name = 'create_user_info'

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.slug = slugify(form.instance.username.username)
        return super(CreateUserInfo, self).form_valid(form)


class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'souvenirs_app/update_user_info.html'

    def get(self, request, **kwargs):
        try:
            self.model.objects.get(username=self.request.user)
            return super(UpdateUserInfo, self).get(request, **kwargs)
        except self.model.DoesNotExist:
            return redirect(reverse('souvenirs_app:create_user_info'))

    def get_object(self, queryset=None):
        return UserInfo.objects.get(username=self.request.user)


class UserInfoListView(ListView):
    model = UserInfo
    template_name = 'souvenirs_app/user_infos.html'
    context_object_name = 'user_infos'


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = 'souvenirs_app/user_info.html'
    context_object_name = 'user_info'
    slug_url_kwarg = 'user_info_slug'


class MyInfoDetailView(UserInfoDetailView):

    def get(self, request, **kwargs):
        try:
            self.model.objects.get(username=self.request.user)
            return super(UserInfoDetailView, self).get(request, **kwargs)
        except self.model.DoesNotExist:
            return redirect(reverse('souvenirs_app:create_user_info'))

    def get_object(self, queryset=None):
        return UserInfo.objects.get(username=self.request.user)
