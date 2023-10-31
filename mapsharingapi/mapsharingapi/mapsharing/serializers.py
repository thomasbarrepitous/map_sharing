# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Playlist, GeocodePoint


class GeocodePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeocodePoint
        fields = ("id", "latitude", "longitude", "address", "playlist")


class PlaylistSerializer(serializers.ModelSerializer):
    geocode_points = GeocodePointSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ("id", "title", "description", "created_at", "geocode_points")
