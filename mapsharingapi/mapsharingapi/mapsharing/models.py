from django.db import models


class Playlist(models.Model):
    """
    Model representing a playlist of geocode points.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GeocodePoint(models.Model):
    """
    Model representing a geocode point.
    """

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255)
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="geocode_points"
    )

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"
