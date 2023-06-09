# Generated by Django 4.2 on 2023-06-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_is_completed'),
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
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='article',
            name='upvoted_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
