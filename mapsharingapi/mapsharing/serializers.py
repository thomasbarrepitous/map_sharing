from rest_framework import serializers
from .models import Playlist, GeocodePoint, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
        fields = (
            "id",
            "latitude",
            "longitude",
            "address",
            "playlist",
            "point_name",
            "description",
        )


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("id", "title", "description", "created_at", "user")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        return token
