from django.db import models
from django.contrib.auth.models import User


class Souvenir(models.Model):
    """"""

    souvenir_id = models.AutoField(primary_key=True)
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_user')
    send_date = models.DateField(auto_now_add=True)
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_user')
    receive_date = models.DateField(auto_now=True)
    send_user_img = models.ImageField(upload_to='send/', default='no-photo.png', null=True, blank=True)
    receive_user_img = models.ImageField(upload_to='receive/', default='no-photo.png', null=True, blank=True)

    STATUS_CHOICES = (('TR', 'Travelling'), ('RCV', 'Received'))

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Travelling')

    def __str__(self):
        return str(self.souvenir_id)

    class Meta:
        verbose_name = 'Souvenir'
        verbose_name_plural = 'Souvenirs'


class Country(models.Model):
    ''''''

    title = models.CharField(max_length=30)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Countries'


class UserInfo(models.Model):
    ''''''

    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sex = models.CharField(max_length=6, choices=(('MALE', 'male'), ('FEMALE', 'female')))
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='userinfo')
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'User_information'
        verbose_name_plural = 'User_informations'