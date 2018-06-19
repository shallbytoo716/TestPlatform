# Generated by Django 2.0.6 on 2018-06-19 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_article_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改'),
        ),
        migrations.AlterField(
            model_name='article',
            name='release_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间'),
        ),
    ]
