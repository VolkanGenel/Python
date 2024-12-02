from django.urls import path
# from . import views // Alttaki ile aynı şey
from watchlist_app.api import views

urlpatterns = [
    path("stream/", views.streamPlatform_list, name="platform-list"),
    path("stream/<int:id>", views.streamPlatform_details, name="getPlatformById"),
    path("list/", views.WatchListAV.as_view(), name="watch-list"),
    path("<int:pk>", views.WatchDetailAV.as_view(), name="getMovieById")
]
