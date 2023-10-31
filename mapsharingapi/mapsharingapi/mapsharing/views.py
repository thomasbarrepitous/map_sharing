from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Playlist, GeocodePoint
from .serializers import PlaylistSerializer, GeocodePointSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeocodePointViewSet(viewsets.ModelViewSet):
    queryset = GeocodePoint.objects.all()
    serializer_class = GeocodePointSerializer
    permission_classes = [permissions.IsAuthenticated]
