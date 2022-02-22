from datetime import datetime
from django import forms
import extras
from .models import Souvenir, UserInfo

class CreateSouvenirForm(forms.ModelForm):
    '''
    Form for the create a souvenir
    '''
    class Meta:
        model = Souvenir
        fields = ['send_user_message']

class UpdateSouvenirBySendUserForm(forms.ModelForm):
    '''
    Form for the update a souvenir by send_user
    '''
    class Meta:
        model = Souvenir
        fields = ['send_user_message', 'send_user_img']


class UpdateSouvenirByReceiveUserForm(forms.ModelForm):
    '''
    Form for the update a souvenir by receive_user
    '''
    class Meta:
        model = Souvenir
        fields = ['receive_user_message', 'receive_user_img']


class UserInfoForm(forms.ModelForm):
    '''
    Form for the add user information
    '''
 
    class Meta:
        model = UserInfo
        exclude = ['username', 'slug']
