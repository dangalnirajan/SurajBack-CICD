# Generated by Django 4.2 on 2023-06-09 07:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0006_remove_article_downvoted_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='downvoted_by',
        ),
        migrations.RemoveField(
            model_name='article',
            name='upvoted_by',
        ),
        migrations.AddField(
            model_name='article',
            name='downvoted_by',
            field=models.ManyToManyField(blank=True, related_name='downvoted_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='upvoted_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
