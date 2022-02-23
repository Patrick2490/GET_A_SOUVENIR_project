from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('souvenirs/', views.ListSouvenirAPIView.as_view(), name='souvenirs'),
    path('souvenirs/<int:pk>/', views.DetailSouvenirAPIView.as_view()),
    path('user_infos/', views.ListUserInfoApiView.as_view(), name='user_infos'),
    path('user_infos/<int:pk>/', views.DetailUserInfoApiView.as_view()),
]