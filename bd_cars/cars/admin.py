from django.contrib import admin

# Register your models here.
from .models import Brand, Car, Purchase, Comment
#register the models to the admin site
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Purchase)
admin.site.register(Comment)