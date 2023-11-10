from rest_framework import viewsets, permissions, status
from .models import Playlist, GeocodePoint, User
from .serializers import PlaylistSerializer, GeocodePointSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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


class GeocodePointViewSet(viewsets.ModelViewSet):
    queryset = GeocodePoint.objects.all()
    serializer_class = GeocodePointSerializer
    permission_classes = [permissions.IsAuthenticated]
