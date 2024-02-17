from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre

from .models import Movie


def movie_listings(request):
    movie_list = Movie.objects.order_by("id")
    context = {"movie_list": movie_list}
    return render(request, "cinemalistings/movie-listings.html", context)


def movie_details(request, movie_id):
    # Get movie_id from 'a' tag in movie-listing.html
    movie = get_object_or_404(Movie, pk=movie_id)

    # Fetch Genre information from Genre table based on movie_id
    genre = Genre.objects.get(id=movie_id).genre

    mpaa_rating = eval(movie.mpaaRating)  # Convert to dict
    mpaa_rating = f"({mpaa_rating['type']}: {mpaa_rating['label']})"

    return render(
        request,
        "cinemalistings/movie-details.html",
        {"movie": movie, "genre": genre, "mpaa_rating": mpaa_rating},
    )
