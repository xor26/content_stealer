# Generated by Django 2.2 on 2019-04-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190403_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='permalink',
            field=models.CharField(default='', max_length=35, primary_key=True, serialize=False),
        ),
    ]
