
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import SongSerializer
from .models import Song
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST']) # handles calling the complete songlist or to create a song
def songs_list(request):
    
    song = Song.objects.all()

    if request.method == 'GET':

        serializer = SongSerializer(song, many=True)

        return Response(serializer.data)


    elif request.method == 'POST':

        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


     