from django.contrib import admin
from .models import Location,Categorie,Image

# Register your models here.

admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Categorie)

