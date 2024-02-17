# Generated by Django 5.0.2 on 2024-02-17 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalistings', '0002_genre_mpaarating_movie_genre_movie_mpaarating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mpaaRating',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='cinemalistings.mpaarating'),
        ),
    ]