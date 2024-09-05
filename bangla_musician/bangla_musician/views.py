from django.shortcuts import render
from musician.models import Musician
from album.models import Album
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def authenticated_home(request):
    if request.user.is_authenticated:
        musicians = Musician.objects.all()
    albums = Album.objects.all()
    context = {
        'musicians': musicians,
        'albums': albums,
    }
    return render(request, 'home.html', context)

def home(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    context = {
        'musicians': musicians,
        'albums': albums,
    }
    return render(request, 'unauthenticated_home.html', context)
