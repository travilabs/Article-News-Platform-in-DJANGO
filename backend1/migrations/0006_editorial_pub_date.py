# Generated by Django 4.2.4 on 2023-09-18 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0005_news_main_article_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorial',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
