# Generated by Django 4.0.2 on 2022-02-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0009_alter_souvenir_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souvenir',
            name='status',
            field=models.CharField(choices=[('ON THE WAY', 'On the way'), ('RECEIVED', 'Received')], default='ON THE WAY', max_length=10),
        ),
    ]
