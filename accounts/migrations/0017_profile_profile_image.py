# Generated by Django 4.1.7 on 2023-04-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='untitled.png', upload_to='profile_images'),
        ),
    ]
