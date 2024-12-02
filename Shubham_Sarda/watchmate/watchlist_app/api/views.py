from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework import status # type: ignore
from rest_framework.views import APIView


# CLASS BASED VIEWS
class WatchListAV(APIView):

    def get(self, request):
       watchLists = WatchList.objects.all() 
       serializer = WatchListSerializer(watchLists, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watchList = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchList)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        watchList = WatchList.objects.get(pk=pk)   
        WatchList.delete(watchList)
        return Response(status=status.HTTP_204_NO_CONTENT)

# FUNCTION BASED VIEWS
@api_view(["GET", "POST"])
def streamPlatform_list(request):
    if request.method== "GET":
        streamPlatforms = StreamPlatform.objects.all()
        # Eğer birden çok obje döneceksek many=True şeklinde işaretleme yapmalıyız.
        serializer = StreamPlatformSerializer(streamPlatforms, many=True)
        return Response(serializer.data)

    if request.method== "POST":
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["GET","PUT","DELETE"])
def streamPlatform_details(request, id):
    if request.method== "GET":
        try:
            streamPlatform = StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamPlatform)
        return Response(serializer.data)
    
    if request.method== "PUT":
        streamPlatform = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSerializer(streamPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method== "DELETE":
        streamPlatform = StreamPlatform.objects.get(id=id)   
        StreamPlatform.delete(streamPlatform)
        return Response(status=status.HTTP_204_NO_CONTENT)



# FUNCTION BASED VIEWS
# @api_view(["GET", "POST"])
# def watchList_list(request):
#     if request.method== "GET":
#         watchLists = WatchList.objects.all()
#         # Eğer birden çok obje döneceksek many=True şeklinde işaretleme yapmalıyız.
#         serializer = WatchListSerializer(watchLists, many=True)
#         return Response(serializer.data)

#     if request.method== "POST":
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=["GET","PUT","DELETE"])
# def watchList_details(request, id):
#     if request.method== "GET":
#         try:
#             watchList = WatchList.objects.get(id=id)
#         except WatchList.DoesNotExist:
#             return Response({"Error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchListSerializer(watchList)
#         return Response(serializer.data)
    
#     if request.method== "PUT":
#         watchList = WatchList.objects.get(id=id)
#         serializer = WatchListSerializer(watchList, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method== "DELETE":
#         watchList = WatchList.objects.get(id=id)   
#         WatchList.delete(watchList)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# İLK KODLAMA
# def watchList_details(request, id):
#     watchList = WatchList.objects.get(id=id)
#     data = {
#         "name" : watchList.name,
#         "description" : watchList.description,
#         "active" : watchList.active
#     }
#     print(watchList.name)
#     return JsonResponse(data)

# def watchList_list(request):
#     watchLists = WatchList.objects.all()
#     data = {
#         "watchLists" : list(watchLists.values())
#     }
#     return JsonResponse(data)