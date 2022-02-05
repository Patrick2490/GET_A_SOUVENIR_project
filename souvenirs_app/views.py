from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

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
    pk_url_kwarg = 'souvenir_id'
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
        return Souvenir.objects.filter(send_user=self.request.user)


class ReceiveUserSouvenirsView(LoginRequiredMixin, ListView):
    model = Souvenir
    template_name = 'souvenirs_app/receive_user_souvenirs.html'
    context_object_name = 'receive_user_souvenirs'

    def get_queryset(self):
        return Souvenir.objects.filter(receive_user=self.request.user)

@login_required
def new_souvenir(request):
    if request.method != 'POST':
        form = SouvenirForm()
    else:
        form = SouvenirForm(request.POST, request.FILES)
        if form.is_valid():
            new_souvenir = form.save(commit=False)
            new_souvenir.send_user = request.user
            new_souvenir.receive_user = random.choice(User.objects.exclude(username=request.user).exclude(username='admin'))
            new_souvenir.extra_name = f'{new_souvenir.send_user}-{UserInfo.objects.get(username=request.user).country.code}'
            new_souvenir.save()
            return redirect('souvenirs_app:souvenirs')
    context = {'form': form}
    return render(request, 'souvenirs_app/new_souvenir.html', context)

@login_required
def user_info(request):
    if request.method != 'POST':
        form = UserInfoForm()
    else:
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.username = request.user
            user_info.save()
            return redirect('souvenirs_app:index')
    context = {'form': form}
    return render(request, 'souvenirs_app/user_info.html', context)



# for generating code
# str(n).zfill(4)
# f'{n:04}'


