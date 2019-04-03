# Generated by Django 2.2 on 2019-04-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('hash', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('title', models.TextField(default='')),
                ('author', models.CharField(default='', max_length=100)),
                ('content', models.TextField(default='')),
                ('upvotes', models.IntegerField(default=0)),
                ('is_posted', models.BooleanField(default=False)),
            ],
        ),
    ]
