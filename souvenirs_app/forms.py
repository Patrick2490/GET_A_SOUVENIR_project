from django import forms
from django.forms import DateInput
from .models import Souvenir, UserInfo

class CreateSouvenirForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['send_user_message']

class UpdateSouvenirBySendUserForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['send_user_message', 'send_user_img']


class UpdateSouvenirByReceiveUserForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['receive_user_message', 'receive_user_img', 'status']


class UserInfoForm(forms.ModelForm):
    date_of_birthday = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
    # slug = forms.SlugField()
    class Meta:
        model = UserInfo
        exclude = ['username', 'slug']
        # widgets = {'date_of_birthday': DateInput(format='%d-%m-%Y')}
