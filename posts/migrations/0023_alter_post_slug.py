# Generated by Django 4.1.7 on 2023-04-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
