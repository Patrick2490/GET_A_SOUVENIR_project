from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from souvenirs_app.models import Souvenir, UserInfo
from .serializers import SouvenirSerializer, UserInfoSerializer
# from .permissions import IsOwnerOrReadOnly

class ListSouvenirAPIView(generics.ListAPIView):
    '''
    Display the entire json-data about souvenirs
    '''
    queryset = Souvenir.objects.all()
    serializer_class = SouvenirSerializer

class DetailSouvenirAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Souvenir.objects.all()
    serializer_class = SouvenirSerializer
    permission_classes = (
        IsAdminUser,
    ) 

class ListUserInfoApiView(generics.ListAPIView):
    '''
    Display the entire json-data about user informations
    '''
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    depth = 1

class DetailUserInfoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    depth = 1
    permission_classes = (
        # IsOwnerOrReadOnly,
        IsAdminUser,
    )