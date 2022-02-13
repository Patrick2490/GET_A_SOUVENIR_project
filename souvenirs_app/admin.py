from django.contrib import admin
from . import models

# admin.site.register(models.Country)
# admin.site.register(models.UserInfo)
# admin.site.register(models.PostCard)

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'slug')
    ordering = ['title']
    prepopulated_fields = {'slug': ('code',)}

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'slug', 'avatar', 'sex', 'date_of_birthday', 'country', 'city', 'address', 'about')
    ordering = ['username']
    prepopulated_fields = {'slug': ('username',)}

@admin.register(models.Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    list_display = ('souvenir_id', 'slug', 'send_user', 'send_date', 'receive_user', 'receive_date', 'send_user_img', 'receive_user_img', 'status')
    ordering = ['souvenir_id']