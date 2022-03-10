from django.forms import ModelFormMetaclass
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
   model = Song
   fields = ['id', 'artist', 'album', 'release_date', 'genre'] 
