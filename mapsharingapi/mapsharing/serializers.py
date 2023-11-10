from rest_framework import serializers
from .models import Playlist, GeocodePoint, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        user.save()
        return user


class GeocodePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeocodePoint
        fields = ("id", "latitude", "longitude", "address", "playlist")


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("id", "title", "description", "created_at", "user")
