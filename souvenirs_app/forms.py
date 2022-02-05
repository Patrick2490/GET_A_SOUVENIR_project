from django import forms

from .models import Souvenir

class SouvenirForm(forms.ModelForm):
    class Meta:
        model = Souvenir
        fields = ['souvenir_id', 'send_user_img', 'receive_user_img']
