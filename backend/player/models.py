from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    duration = models.FloatField()
    spotify_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
