from django.urls import path

from . import views


urlpatterns = [
    path('souvenirs/', views.ListSouvenirAPIView.as_view()),
    path('souvenirs/<int:pk>/', views.DetailSouvenirAPIView.as_view()),
    path('user_infos/', views.ListUserInfoApiView.as_view()),
    path('user_infos/<int:pk>/', views.DetailUserInfoApiView.as_view()),
]