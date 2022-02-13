from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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


# def souvenirs(request):
#     souvenirs = Souvenir.objects.order_by('souvenir_id')
#     context = {'souvenirs': souvenirs}
#     return render(request, 'souvenirs_app/souvenirs.html', context)


class SouvenirView(DetailView):
    model = Souvenir
    # pk_url_kwarg = 'souvenir_id'
    slug_url_kwarg = 'souvenir_slug'
    context_object_name = 'souvenir'
    # souvenir = Souvenir.objects.get(souvenir_id=pk)
    template_name = 'souvenirs_app/souvenir.html'

# @login_required
# def souvenir(request, souvenir_id):
#     souvenir = Souvenir.objects.get(souvenir_id=souvenir_id)
#     details = f'Souvenir #{souvenir.souvenir_id} sent by {souvenir.send_user} to {souvenir.receive_user} on {souvenir.send_date}'
#     status = souvenir.status
#     image = souvenir.receive_user_img
#     context = {'souvenir_details': details, 'souvenir_status': status, 'souvenir_image': image}
#     return render(request, 'souvenirs_app/souvenir.html', context)


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
        form.instance.slug = f'{UserInfo.objects.get(username=form.instance.send_user).country.code}{random_number}{UserInfo.objects.get(username=form.instance.receive_user).country.code}'
        return super(CreateSouvenir, self).form_valid(form)


# @login_required
# def new_souvenir(request):
#     if request.method != 'POST':
#         form = SouvenirForm()
#     else:
#         form = SouvenirForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_souvenir = form.save(commit=False)
#             # new_souvenir.souvenir_id = souvenir_id
#             new_souvenir.send_user = request.user
#             new_souvenir.receive_user = random.choice(User.objects.exclude(username=request.user).exclude(username='admin'))
#             new_souvenir.slug = f'{UserInfo.objects.get(username=new_souvenir.send_user).country.code}--{UserInfo.objects.get(username=new_souvenir.receive_user).country.code}'
#             print(new_souvenir.slug)
#             print(new_souvenir.souvenir_id, Souvenir.objects.get(souvenir_id=new_souvenir))
#             new_souvenir.save()
#             return redirect('souvenirs_app:souvenirs')
#     context = {'form': form}
#     return render(request, 'souvenirs_app/create_souvenir.html', context)


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

    def get_object(self, queryset=None):
        return UserInfo.objects.get(username=self.request.user)


# @login_required
# def new_user_info(request):
#     if request.method != 'POST':
#         form = UserInfoForm()
#     else:
#         form = UserInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_user_info = form.save(commit=False)
#             new_user_info.username = request.user
#             new_user_info.save()
#             return redirect('souvenirs_app:index')
#     context = {'form': form}
#     return render(request, 'souvenirs_app/create_user_info.html', context)


class UserInfoListView(ListView):
    model = UserInfo
    template_name = 'souvenirs_app/user_infos.html'
    context_object_name = 'user_infos'


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    model = UserInfo
    template_name = 'souvenirs_app/user_info.html'
    context_object_name = 'user_info'
    slug_url_kwarg = 'user_info_slug'

    # def get_object(self, queryset=None):
    #     return UserInfo.objects.get(username=self.request.user)


    # def get(self, request):
    #     my_user_info = UserInfo.objects.get(slug=self.request.user)
    #     return render(request, 'souvenirs_app/user_info.html', {'my_user_info': my_user_info})


# for generating code
# str(n).zfill(4)
# f'{n:04}'


