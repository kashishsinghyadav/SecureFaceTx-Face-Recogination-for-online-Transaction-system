# Generated by Django 4.2.2 on 2024-03-03 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job',
        ),
    ]
