# Generated by Django 2.2 on 2019-04-03 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190403_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='link',
            new_name='permalink',
        ),
    ]
