# Generated by Django 4.0.2 on 2022-02-13 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0004_souvenir_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souvenir',
            name='receive_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_user', to='souvenirs_app.userinfo'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='send_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_user', to='souvenirs_app.userinfo'),
        ),
    ]
