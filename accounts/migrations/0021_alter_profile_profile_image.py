# Generated by Django 4.1.7 on 2023-04-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_liked_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='broktuvjt94q9ob2obxt', upload_to='profile_images'),
        ),
    ]
