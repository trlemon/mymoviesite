from django.urls import path

from . import views

urlpatterns = [
    path("", views.movie_listings, name="movie-listings"),
    path("<int:movie_id>/", views.movie_details, name="movie-details"),
]
