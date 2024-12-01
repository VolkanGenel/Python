from django.urls import path
# from . import views // Alttaki ile aynı şey
from watchlist_app.api import views

urlpatterns = [
    # path("list/", views.movie_list, name="movie-list"),
    # path("<int:id>", views.movie_details, name="getMovieById")
    path("list/", views.MovieListAV.as_view(), name="movie-list"),
    path("<int:pk>", views.MovieDetailAV.as_view(), name="getMovieById")
]
