# Generated by Django 4.1.7 on 2023-04-08 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0016_remove_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]