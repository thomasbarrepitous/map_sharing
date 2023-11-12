from rest_framework import viewsets, permissions, status
from .models import Playlist, GeocodePoint, User
from .serializers import (
    PlaylistSerializer,
    GeocodePointSerializer,
    UserSerializer,
    MyTokenObtainPairSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PlaylistSerializer(
            data={
                "user": user.id,
                "title": request.data.get("title"),
                "description": request.data.get("description"),
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "Playlist could not be created"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["get"], url_path="geocode-points")
    def geocode_points(self, request, pk=None):
        playlist = self.get_object()
        geocode_points = GeocodePoint.objects.filter(playlist=playlist)
        serializer = GeocodePointSerializer(geocode_points, many=True)
        return Response(serializer.data)


# TODO: Modify the ViewSet to only allow retrieve() for the user that created the playlist
class GeocodePointViewSet(viewsets.ModelViewSet):
    queryset = GeocodePoint.objects.all()
    serializer_class = GeocodePointSerializer
    permission_classes = [permissions.IsAuthenticated]


# Override the TokenObtainPairView class to return the user id
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
