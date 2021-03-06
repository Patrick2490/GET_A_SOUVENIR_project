# Generated by Django 4.0.2 on 2022-02-08 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('slug', models.SlugField(max_length=3, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
                ('avatar', models.ImageField(blank=True, default='no-avatar.jpg', null=True, upload_to='avatars/')),
                ('sex', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=6)),
                ('date_of_birthday', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=200)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userinfo', to='souvenirs_app.country')),
            ],
            options={
                'verbose_name': 'User_information',
                'verbose_name_plural': 'User_informations',
            },
        ),
        migrations.CreateModel(
            name='Souvenir',
            fields=[
                ('souvenir_id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
                ('send_date', models.DateField(auto_now_add=True)),
                ('receive_date', models.DateField(auto_now=True)),
                ('send_user_img', models.ImageField(blank=True, default='no-photo.png', null=True, upload_to='send/')),
                ('receive_user_img', models.ImageField(blank=True, default='no-photo.png', null=True, upload_to='receive/')),
                ('status', models.CharField(choices=[('TR', 'Travelling'), ('RCV', 'Received')], default='Travelling', max_length=10)),
                ('extra_name', models.CharField(default='', max_length=10)),
                ('receive_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_user', to=settings.AUTH_USER_MODEL)),
                ('send_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Souvenir',
                'verbose_name_plural': 'Souvenirs',
            },
        ),
    ]
