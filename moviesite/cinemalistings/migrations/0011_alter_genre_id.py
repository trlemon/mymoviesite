# Generated by Django 5.0.2 on 2024-02-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalistings', '0010_remove_movie_genre_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]