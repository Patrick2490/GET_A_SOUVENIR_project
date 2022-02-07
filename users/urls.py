from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('log_out/', views.logout_view, name='logout'),
]