from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Libro


# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "idioma",
        "fecha_publicacion",
        "portada",
    ]


admin.site.register(Libro, LibroAdmin)
admin.site.register(Permission)
