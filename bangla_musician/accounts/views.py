from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from musician.models import Musician
from album.models import Album

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# @method_decorator(login_required, name='dispatch')
# def profile(request):
#     musicians = Musician.objects.all()
#     albums = Album.objects.all()
#     context = {
#         'musicians': musicians,
#         'albums': albums,
#     }
#     return render(request, 'home.html', context)
