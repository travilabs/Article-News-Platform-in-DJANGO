# Generated by Django 4.2.4 on 2023-09-19 14:50

import backend1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0009_alter_newestcourse_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hashtags',
            field=models.ManyToManyField(default=backend1.models.python_default, to='backend1.hashtag'),
        ),
        migrations.AddField(
            model_name='cryptoanalysis',
            name='hashtags',
            field=models.ManyToManyField(default=backend1.models.python_default, to='backend1.hashtag'),
        ),
    ]
