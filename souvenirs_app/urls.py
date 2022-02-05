from django.urls import path, include

from . import views

app_name = 'souvenirs_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('souvenirs/', views.SouvenirsView.as_view(), name='souvenirs'),
    path('souvenirs/<int:souvenir_id>/', views.SouvenirView.as_view(), name='souvenir'),
    path('new_souvenir/', views.new_souvenir, name='new_souvenir'),
]