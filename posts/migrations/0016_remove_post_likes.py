# Generated by Django 4.1.7 on 2023-04-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_post_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
