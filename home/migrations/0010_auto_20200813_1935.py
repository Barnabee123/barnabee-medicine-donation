# Generated by Django 3.1 on 2020-08-13 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_donations_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdonor',
            name='date',
        ),
        migrations.RemoveField(
            model_name='userngo',
            name='date',
        ),
    ]
