from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    '''
    Model for the country of the user
    '''
    title = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=3, unique=True)
    slug = models.SlugField(max_length=3, verbose_name='URL')

    def __str__(self):
        '''Return the title of country'''
        return self.title

    class Meta:
        '''
        Change the display of instances in a table
        '''
        verbose_name_plural = 'Countries'


class UserInfo(models.Model):
    '''
    Model for the detailed information about the user
    '''
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
        '''
        Returns the username of userinfo
        '''
        return str(self.username)

    def get_absolute_url(self):
        '''
        Generates a URL for the model object
        '''
        return reverse('souvenirs_app:user_info', kwargs={'user_info_slug': self.slug})

    def send_count(self):
        return UserInfo.objects.get(slug = self.slug).send_user.all().count()

    def receive_count(self):
        return UserInfo.objects.get(slug = self.slug).receive_user.all().count()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.username)
    #     super(UserInfo, self).save(*args, **kwargs)

    class Meta:
        '''
        Change the display of instances in a table
        '''
        verbose_name = 'User_information'
        verbose_name_plural = 'User_informations'


class Souvenir(models.Model):
    """
    Model for the souvenirs
    """
    souvenir_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=30, verbose_name='URL')
    send_user = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='send_user')
    send_date = models.DateField(auto_now_add=True)
    receive_user = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='receive_user')
    receive_date = models.DateField(null=True, blank=True)
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
        '''
        Returns the souvenir_id
        '''
        return str(self.souvenir_id)

    def get_absolute_url(self):
        '''
        Generates a URL for the model object
        '''
        return reverse('souvenirs_app:souvenir', kwargs={'souvenir_slug': self.slug})

    def on_the_way(self):
        '''
        Calculates the souvenir on the way time
        '''
        return f'{(self.receive_date - self.send_date).days} days'

    class Meta:
        '''
        Change the display of instances in a table
        '''
        verbose_name = 'Souvenir'
        verbose_name_plural = 'Souvenirs'
