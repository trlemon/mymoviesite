# Generated by Django 5.0.2 on 2024-02-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalistings', '0014_remove_movie_genre_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]