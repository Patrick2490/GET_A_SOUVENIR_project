# Generated by Django 4.0.2 on 2022-02-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0012_alter_souvenir_receive_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souvenir',
            name='receive_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]