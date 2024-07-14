# Generated by Django 5.0.6 on 2024-07-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=128),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default='defaultusername', max_length=150, unique=True),
        ),
    ]
