# Generated by Django 5.0.2 on 2024-02-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalistings', '0017_delete_mpaarating_movie_mpaarating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mpaaRating',
            field=models.TextField(),
        ),
    ]
