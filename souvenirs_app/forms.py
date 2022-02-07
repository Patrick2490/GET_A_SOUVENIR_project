from django import forms
from django.forms import DateInput
from .models import Souvenir, UserInfo

class SouvenirForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['souvenir_id', 'send_user_img', 'receive_user_img']



class UserInfoForm(forms.ModelForm):
    date_of_birthday = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'))
    class Meta:
        model = UserInfo
        exclude = ['username']
        # widgets = {'date_of_birthday': DateInput(format='%d-%m-%Y')}

