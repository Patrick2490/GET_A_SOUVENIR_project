from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    ''''''

    title = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=3, unique=True)
    slug = models.SlugField(max_length=3, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Countries'


class UserInfo(models.Model):
    ''''''

    username = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    slug = models.SlugField(max_length=30, verbose_name='URL')
    avatar = models.ImageField(upload_to='avatars/', default='no-avatar.jpg', null=True, blank=True)
    sex = models.CharField(max_length=6, choices=(('MALE', 'male'), ('FEMALE', 'female')))
    date_of_birthday = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='userinfo', unique=False)
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    about = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('souvenirs_app:user_info', kwargs={'user_info_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.username)
    #     super(UserInfo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User_information'
        verbose_name_plural = 'User_informations'


class Souvenir(models.Model):
    """"""

    souvenir_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=30, verbose_name='URL')
    send_user = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='send_user')
    send_date = models.DateField(auto_now_add=True)
    receive_user = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='receive_user')
    receive_date = models.DateField()
    send_user_img = models.ImageField(upload_to='send/', default='no-photo.png', null=True, blank=True)
    receive_user_img = models.ImageField(upload_to='receive/', default='no-photo.png', null=True, blank=True)
    send_user_message = models.TextField(max_length=500, null=True, blank=True)
    receive_user_message = models.TextField(max_length=500, null=True, blank=True)

    STATUS_CHOICES = [
        ('ON THE WAY', 'On the way'),
        ('RECEIVED', 'Received'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ON THE WAY')

    def __str__(self):
        return str(self.souvenir_id)

    def get_absolute_url(self):
        return reverse('souvenirs_app:souvenir', kwargs={'souvenir_slug': self.slug})

    def on_the_way(self):
        return f'{(self.receive_date - self.send_date).days} days'

    class Meta:
        verbose_name = 'Souvenir'
        verbose_name_plural = 'Souvenirs'
