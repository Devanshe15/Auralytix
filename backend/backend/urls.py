from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Default home route
def home(request):
    return JsonResponse({"message": "Welcome to Auralytix API!"})

urlpatterns = [
    path('', home),  # Set a default home page
    path('api/', include('player.urls')),  # Your API endpoints
    path('admin/', admin.site.urls),
]
