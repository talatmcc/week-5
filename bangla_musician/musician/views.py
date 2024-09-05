from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicianForm

def create_musician(request):
    if request.method == 'POST':
        # print("POST")
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = MusicianForm()
    return render(request, 'musician/create_musician.html', {'form': form})


def edit_musician(request, id):
    musician = Musician.objects.get(id=id)
    print(musician)
    form = MusicianForm(instance=musician)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
        return redirect("home")
    return render(request, "./musician/edit_musician.html", {"form": form})


def delete_musician(request, id):
    musician = Musician.objects.filter(id=id)
    musician.delete()
    return redirect("home")
