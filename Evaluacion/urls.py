from django.contrib import admin
from django.urls import path, include
from libreria import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("libros/", views.listadoLibros),
    path("agregar/", views.agregarLibro),
    path("eliminar/<int:id>", views.eliminarLibro),
    path("actualizar/<int:id>", views.actualizarLibro),
    path("librosapi/", views.libro_list),
    path("librosapi/<int:pk>", views.libro_detail),
]


# Config para servir statics y medias de pana
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
