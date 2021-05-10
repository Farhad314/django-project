from django.shortcuts import render

from .models import Album

def albumHome(request):
    albums = Album.objects.all()
    context = {
        "albums": albums

    }
    return render(request, 'album/index.html', context)