# Generated by Django 5.0.2 on 2024-02-17 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalistings', '0004_remove_movie_mpaarating_delete_mpaarating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre',
        ),
    ]
