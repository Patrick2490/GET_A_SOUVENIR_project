from django.urls import path, include

from . import views

app_name = 'souvenirs_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('souvenirs/', views.SouvenirsView.as_view(), name='souvenirs'),
    path('souvenirs/<slug:souvenir_slug>/', views.SouvenirView.as_view(), name='souvenir'),
    path('create_souvenir/', views.CreateSouvenir.as_view(), name='create_souvenir'),
    path('update_souvenir/<slug:souvenir_slug>/', views.UpdateSouvenir.as_view(), name='update_souvenir'),
    path('send_user_souvenirs/', views.SendUserSouvenirsView.as_view(), name='send_user_souvenirs'),
    path('receive_user_souvenirs/', views.ReceiveUserSouvenirsView.as_view(), name='receive_user_souvenirs'),
    path('user_infos/', views.UserInfoListView.as_view(), name='user_infos'),
    path('user_info/<slug:user_info_slug>/', views.UserInfoDetailView.as_view(), name='user_info'),
    path('create_user_info/', views.CreateUserInfo.as_view(), name='create_user_info'),
    path('update_user_info/<slug:user_info_slug>/', views.UpdateUserInfo.as_view(), name='update_user_info'),
    path('my_info/<slug:user_info_slug>/', views.MyInfoDetailView.as_view(), name='my_info'),
]
