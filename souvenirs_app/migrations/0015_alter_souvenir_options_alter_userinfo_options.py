# Generated by Django 4.0.2 on 2022-02-24 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0014_alter_country_options_alter_souvenir_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='souvenir',
            options={'ordering': ['send_date', 'souvenir_id'], 'verbose_name': 'Souvenir', 'verbose_name_plural': 'Souvenirs'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['slug'], 'verbose_name': 'User_information', 'verbose_name_plural': 'User_informations'},
        ),
    ]