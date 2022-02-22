from email import message
from multiprocessing import context
from pyexpat import model
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.text import slugify

from django.contrib.auth.models import User
from .models import Souvenir, UserInfo, Country
from .forms import CreateSouvenirForm, UserInfoForm, UpdateSouvenirBySendUserForm, UpdateSouvenirByReceiveUserForm
from .permissions import SendUserChangePermissionsMixin, ReceiveUserChangePermissionsMixin

from datetime import date
import random


def index(request):
    '''
    View for the homepage
    '''
    return render(request, 'souvenirs_app/index.html')


class SouvenirsView(ListView):
    '''
    View for all souvenirs
    '''
    model = Souvenir
    template_name = 'souvenirs_app/souvenirs.html'
    context_object_name = 'souvenirs'


class SearchSouvenir(SouvenirsView):
    '''
    View for found souvenirs
    '''
    template_name = 'souvenirs_app/search_list.html'

    def get_queryset(self):
        '''
        Return found souvenirs
        '''
        return Souvenir.objects.filter(slug__exact=self.request.GET.get('search'))


class SendUserSouvenirsView(LoginRequiredMixin, SouvenirsView):
    '''
    View for the souvenirs send by user
    '''
    template_name = 'souvenirs_app/send_user_souvenirs.html'
    context_object_name = 'send_user_souvenirs'

    def get_queryset(self):
        '''
        Return souvenirs send by user
        '''
        return Souvenir.objects.filter(send_user__slug=slugify(self.request.user), status='RECEIVED')


class OnTheWayUserSouvenirsView(LoginRequiredMixin, SouvenirsView):
    '''
    View for the on the way souvenirs send by user
    '''
    template_name = 'souvenirs_app/send_user_souvenirs.html'
    context_object_name = 'send_user_souvenirs'

    def get_queryset(self):
        '''
        Return on the way souvenirs send by user
        '''
        return Souvenir.objects.filter(send_user__slug=slugify(self.request.user), status='ON THE WAY')


class ReceiveUserSouvenirsView(LoginRequiredMixin, SouvenirsView):
    '''
    View for the souvenirs received by user
    '''
    template_name = 'souvenirs_app/receive_user_souvenirs.html'
    context_object_name = 'receive_user_souvenirs'

    def get_queryset(self):
        '''
        Return souvenirs received by user
        '''
        return Souvenir.objects.filter(receive_user__slug=slugify(self.request.user), status='RECEIVED')


class SouvenirView(DetailView):
    '''
    View for the detail information of the souvenir
    '''
    model = Souvenir
    slug_url_kwarg = 'souvenir_slug'
    context_object_name = 'souvenir'
    template_name = 'souvenirs_app/souvenir.html'


class CreateSouvenir(LoginRequiredMixin, CreateView):
    '''
    View for the create a souvenir
    '''
    model = Souvenir
    form_class = CreateSouvenirForm
    template_name = 'souvenirs_app/create_souvenir.html'
    context_object_name = 'create_souvenir'
    initial = {'send_user_message': 'Hello! I am very happy to send a souvenir for you!'}

    def form_valid(self, form):
        '''
        Function of checking valid and set default attribute values
        '''
        form.instance.send_user = UserInfo.objects.get(username=self.request.user)
        form.instance.receive_user = random.choice(UserInfo.objects.exclude(country=self.request.user.userinfo.country))
        random_number = str(random.randint(0, 99999)).zfill(5)
        form.instance.slug = f'{UserInfo.objects.get(username=form.instance.send_user).country.code}' \
                             f'{random_number}' \
                             f'{UserInfo.objects.get(username=form.instance.receive_user).country.code}'
        return super(CreateSouvenir, self).form_valid(form)


class UpdateSouvenirBySendUser(SendUserChangePermissionsMixin, UpdateView):
    '''
    View for the update souvenir information by send_user
    '''
    # permission_required = 'souvenirs_app.change_souvenir'
    model = Souvenir
    form_class = UpdateSouvenirBySendUserForm
    template_name = 'souvenirs_app/update_souvenir_by_send_user.html'
    slug_url_kwarg = 'souvenir_slug'



class UpdateSouvenirByReceiveUser(ReceiveUserChangePermissionsMixin, UpdateView):
    '''
    View for the update souvenir information by receive_user
    '''
    model = Souvenir
    form_class = UpdateSouvenirByReceiveUserForm
    template_name = 'souvenirs_app/update_souvenir_by_receive_user.html'
    slug_url_kwarg = 'souvenir_slug'
    initial = {'receive_user_message': 'Thank you for the souvenir!'}

    def form_valid(self, form):
        '''
        Function of checking valid and set attribute values
        '''
        self.object.receive_date = date.today()
        self.object.status = 'RECEIVED'
        # print(self.object.receive_date, self.object.status)
        return super().form_valid(form)


class CreateUserInfo(LoginRequiredMixin, CreateView):
    '''
    View for create user information
    '''
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'souvenirs_app/create_user_info.html'
    context_object_name = 'create_user_info'

    def form_valid(self, form):
        '''
        Function of checking valid and set default attribute values
        '''
        form.instance.username = self.request.user
        form.instance.slug = slugify(form.instance.username.username)
        return super(CreateUserInfo, self).form_valid(form)


class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    '''
    View for update user information
    '''
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'souvenirs_app/update_user_info.html'

    def get(self, request, **kwargs):
        '''
        Return Update if True and Create if False
        '''
        try:
            self.model.objects.get(username=self.request.user)
            return super(UpdateUserInfo, self).get(request, **kwargs)
        except self.model.DoesNotExist:
            return redirect(reverse('souvenirs_app:create_user_info'))

    def get_object(self, queryset=None):
        '''
        Return user information of autheticated user
        '''
        return UserInfo.objects.get(username=self.request.user)


class UserInfoListView(ListView):
    '''
    View for informations off all users
    '''
    model = UserInfo
    template_name = 'souvenirs_app/user_infos.html'
    context_object_name = 'user_infos'


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    '''
    View for the detail information of the user
    '''
    model = UserInfo
    template_name = 'souvenirs_app/user_info.html'
    context_object_name = 'user_info'
    slug_url_kwarg = 'user_info_slug'


class MyInfoDetailView(UserInfoDetailView):
    '''
    View for the detail information of autheticated user
    '''
    def get(self, request, **kwargs):
        '''
        Return DetailView if True and Create if False
        '''
        try:
            self.model.objects.get(username=self.request.user)
            return super(UserInfoDetailView, self).get(request, **kwargs)
        except self.model.DoesNotExist:
            return redirect(reverse('souvenirs_app:create_user_info'))

    def get_object(self, queryset=None):
        '''
        Return user information of autheticated user
        '''
        return UserInfo.objects.get(username=self.request.user)
