# Generated by Django 4.1.7 on 2023-04-07 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
