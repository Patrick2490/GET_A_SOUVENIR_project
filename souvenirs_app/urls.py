from django.urls import path, include

from . import views

app_name = 'souvenirs_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('souvenirs/', views.SouvenirsView.as_view(), name='souvenirs'),
    path('souvenirs/<int:souvenir_id>/', views.SouvenirView.as_view(), name='souvenir'),
    path('new_souvenir/', views.new_souvenir, name='new_souvenir'),
    path('new_user_info/', views.new_user_info, name='new_user_info'),
    path('user_info/', views.UserInfoDetailView.as_view(), name='user_info'),
    path('send_user_souvenirs/', views.SendUserSouvenirsView.as_view(), name='send_user_souvenirs'),
    path('receive_user_souvenirs/', views.ReceiveUserSouvenirsView.as_view(), name='receive_user_souvenirs'),
]