# from django.http import JsonResponse
# from django.shortcuts import render
# from watchlist_app.models import Movie
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         "movies" : list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_details(request, id):
#     movie = Movie.objects.get(id=id)
#     data = {
#         "name" : movie.name,
#         "description" : movie.description,
#         "active" : movie.active
#     }
#     print(movie.name)
#     return JsonResponse(data)