# Generated by Django 4.0.2 on 2022-02-09 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0002_alter_country_slug_alter_souvenir_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='souvenir',
            name='extra_name',
        ),
    ]
