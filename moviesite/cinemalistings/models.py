from django.db import models
import re


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    imgPath = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    language = models.CharField(max_length=30)

    # importing mpaaRating as text field which avoids blank import
    # issue I had while importing into MPAARating Model with admin dashboard.
    # I realize this is not ideal, but this is all I could figure out with the
    # time contraints I have.
    mpaaRating = models.TextField()

    userRating = models.CharField(max_length=10)


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def clean_data(self):
        # remove braces and quotes to match prompt format
        self.genre = re.sub(r"['\"\[\]]", "", str(self.genre))

    def save(self, *args, **kwargs):
        self.clean_data()
        super().save(*args, **kwargs)
