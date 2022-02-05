from django.contrib import admin
from . import models

# admin.site.register(models.Country)
# admin.site.register(models.UserInfo)
# admin.site.register(models.PostCard)

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    ordering = ['title']

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'sex', 'age', 'country', 'city', 'address')
    ordering = ['username']

@admin.register(models.Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    list_display = ('souvenir_id', 'send_user', 'send_date', 'receive_user', 'receive_date', 'send_user_img', 'receive_user_img', 'status')
    ordering = ['souvenir_id']