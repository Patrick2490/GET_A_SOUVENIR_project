from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from souvenirs_app.models import Souvenir, UserInfo


class SouvenirSerializer(serializers.ModelSerializer):
    '''
    Selection of model and fields to be serialized in Json format.
    '''
    class Meta:
        model = Souvenir
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    '''
    Selection of model and fields to be serialized in Json format.
    '''
    country = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserInfo
        fields = '__all__'    
