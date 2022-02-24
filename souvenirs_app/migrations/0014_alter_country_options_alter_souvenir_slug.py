# Generated by Django 4.0.2 on 2022-02-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0013_alter_souvenir_receive_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['title'], 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='slug',
            field=models.SlugField(max_length=30, unique=True, verbose_name='URL'),
        ),
    ]