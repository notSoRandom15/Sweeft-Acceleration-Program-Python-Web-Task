# Generated by Django 5.0.3 on 2024-03-09 11:09

import users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]