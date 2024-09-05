from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticated_home', views.authenticated_home, name='authenticated_home'),
    path('', views.home, name='home'),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
