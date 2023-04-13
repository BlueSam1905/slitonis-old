# Generated by Django 4.1.7 on 2023-04-05 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='none', max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='none', max_length=200, null=True, unique=True),
        ),
    ]