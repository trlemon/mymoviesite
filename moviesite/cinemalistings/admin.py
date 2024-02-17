from django.contrib import admin
from .models import Movie, Genre
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Movie object
class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie


class MovieAdmin(ImportExportModelAdmin):
    resources_class = MovieResource


# Genre object
class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    resources_class = GenreResource


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
