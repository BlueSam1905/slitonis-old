# Generated by Django 4.1.7 on 2023-04-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='Untitled.png', upload_to='profile_images'),
        ),
    ]
