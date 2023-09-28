# Generated by Django 4.2.4 on 2023-09-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0003_remove_news_featured_news_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='position',
        ),
        migrations.AddField(
            model_name='news',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
