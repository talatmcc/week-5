from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = AlbumForm()
    return render(request, 'album/create_album.html', {'form': form})


def edit_album(request, id):
    album = Album.objects.filter(id=id).first()
    form = AlbumForm(instance=album)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
        return redirect("home")
    return render(request, "./album/edit_album.html", {"form": form})


def delete_album(request, id):
    album = Album.objects.filter(id=id)
    album.delete()
    return redirect("home")
