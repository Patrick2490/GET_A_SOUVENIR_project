# Generated by Django 4.0.2 on 2022-02-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0007_remove_souvenir_slug_souvenir_extra_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, default='no-avatar.png', null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='date_of_birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
