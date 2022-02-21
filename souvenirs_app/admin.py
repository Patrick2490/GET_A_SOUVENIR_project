from django.contrib import admin
from . import models

# admin.site.register(models.Country)
# admin.site.register(models.UserInfo)
# admin.site.register(models.PostCard)

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    '''
    Class for display model Country for admin
    '''
    list_display = ('title', 'code', 'slug')
    ordering = ['title']
    prepopulated_fields = {'slug': ('code',)}

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    '''
    Class for display model UserInfo for admin
    '''
    list_display = ('username', 'slug', 'avatar', 'sex', 'date_of_birthday', 'country', 'city', 'address', 'about')
    ordering = ['username']
    prepopulated_fields = {'slug': ('username',)}

@admin.register(models.Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    '''
    Class for display model Souvenir for admin
    '''
    list_display = ('souvenir_id', 'slug', 'send_user', 'send_date', 'receive_user', 'receive_date','status', 'send_user_message', 'send_user_img', 'receive_user_message', 'receive_user_img')
    ordering = ['souvenir_id']
    