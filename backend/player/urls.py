from django.urls import path
from .views import get_spotify_tracks

urlpatterns = [
    path('spotify/', get_spotify_tracks),
]
