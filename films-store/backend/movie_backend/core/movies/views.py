from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework import generics 
from rest_framework import viewsets 

from .models import Movies

from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    image = serializers.ImageField(required=False) #make it optional
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    # get moviews 
    # def list(self, request):
    #     movies = Movies.objects.all()
    #     serializer = MovieSerializer(movies, many=True)
    #     return HttpResponse(serializer.data)
    
    # # get movie by id
    # def retrieve(self, request, pk=None):
    #     movie = Movies.objects.get(id=pk)
    #     serializer = MovieSerializer(movie)
    #     return HttpResponse(serializer.data)
    
    # # create 
    # def create(self, request):
    #     serializer = MovieSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return HttpResponse(serializer.data)

    # # update
    # def update(self, request, pk=None):
    #     movie = Movies.objects.get(id=pk)
    #     serializer = MovieSerializer(instance=movie, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return HttpResponse(serializer.data)

    # # delete
    # def destroy(self, request, pk=None):
    #     movie = Movies.objects.get(id=pk)
    #     movie.delete()
    #     return HttpResponse(status=204)



# class MovieCreateAPIView(generics.CreateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer


# class MovieAPIView(generics.ListAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer


# class MovieDetailAPIView(generics.RetrieveAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer



