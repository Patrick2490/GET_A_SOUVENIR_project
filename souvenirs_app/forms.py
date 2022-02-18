from django import forms
from django.forms import DateInput
from .models import Souvenir, UserInfo

class CreateSouvenirForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['message']

class UpdateSouvenirForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['message', 'send_user_img', 'receive_user_img']


class UserInfoForm(forms.ModelForm):
    date_of_birthday = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
    # slug = forms.SlugField()
    class Meta:
        model = UserInfo
        exclude = ['username', 'slug']
        # widgets = {'date_of_birthday': DateInput(format='%d-%m-%Y')}
