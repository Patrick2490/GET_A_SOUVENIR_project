# Generated by Django 4.0.2 on 2022-02-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souvenirs_app', '0010_alter_souvenir_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='souvenir',
            old_name='message',
            new_name='send_user_message',
        ),
        migrations.AddField(
            model_name='souvenir',
            name='receive_user_message',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
