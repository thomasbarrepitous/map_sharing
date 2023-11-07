from rest_framework import viewsets
from rest_framework import permissions
from .models import Playlist, GeocodePoint
from .serializers import PlaylistSerializer, GeocodePointSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeocodePointViewSet(viewsets.ModelViewSet):
    queryset = GeocodePoint.objects.all()
    serializer_class = GeocodePointSerializer
    permission_classes = [permissions.IsAuthenticated]
