import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

# Set up Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET
))

@api_view(['GET'])
def get_spotify_tracks(request):
    query = request.GET.get('query', 'lofi')  # Default search term
    results = sp.search(q=query, limit=10, type='track')
    
    songs = []
    for track in results['tracks']['items']:
        songs.append({
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'spotify_url': track['external_urls']['spotify'],
            'preview_url': track['preview_url'],
            'album_image': track['album']['images'][0]['url']
        })
    
    return Response(songs)
