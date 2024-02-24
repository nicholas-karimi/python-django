from rest_framework import serializers 
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

from .models import Movies


class MovieSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(default=[])

    class Meta:
        model = Movies
        fields = '__all__'
