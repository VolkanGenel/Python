# from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie
from rest_framework import status # type: ignore
from rest_framework.views import APIView


# CLASS BASED VIEWS
class MovieListAV(APIView):

    def get(self, request):
       movies = Movie.objects.all() 
       serializer = MovieSerializer(movies, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)   
        Movie.delete(movie)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# FUNCTION BASED VIEWS
# @api_view(["GET, "POST"])
# def movie_list(request):
#     if request.method== "GET":
#         movies = Movie.objects.all()
#         # Eğer birden çok obje döneceksek many=True şeklinde işaretleme yapmalıyız.
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method== "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=["GET","PUT","DELETE"])
# def movie_details(request, id):
#     if request.method== "GET":
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method== "PUT":
#         movie = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method== "DELETE":
#         movie = Movie.objects.get(id=id)   
#         Movie.delete(movie)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# İLK KODLAMA
# def movie_details(request, id):
#     movie = Movie.objects.get(id=id)
#     data = {
#         "name" : movie.name,
#         "description" : movie.description,
#         "active" : movie.active
#     }
#     print(movie.name)
#     return JsonResponse(data)

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         "movies" : list(movies.values())
#     }
#     return JsonResponse(data)