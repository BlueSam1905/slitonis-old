# Generated by Django 4.1.7 on 2023-04-08 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_liked_post_likedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_post',
            name='likedby',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
