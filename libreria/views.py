from http import server
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import LibroSerializer
from . import forms
from .models import Libro
from rest_framework import viewsets


def index(request):
    return render(request, "index.html")


# View Set
class LibroViewSets(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# Funciones Libros
@permission_required("libreria.view_libro")
def listadoLibros(request):
    libros = Libro.objects.all()
    data = {"libros": libros}
    return render(request, "libros.html", data)


@permission_required("libreria.add_libro")
def agregarLibro(request):
    form = forms.RegistroLibroForm()
    if request.method == "POST":
        form = forms.RegistroLibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/libros")
    data = {"form": form}
    return render(request, "agregar.html", data)


@permission_required("libreria.delete_libro")
def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect("/libros")


@permission_required("libreria.change_libro")
def actualizarLibro(request, id):
    libro = Libro.objects.get(id=id)
    form = forms.RegistroLibroForm(instance=libro)
    if request.method == "POST":
        form = forms.RegistroLibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return listadoLibros(request)
    data = {"form": form}
    return render(request, "agregar.html", data)


# RestAPI Functions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@permission_required("libreria.view_libro")
@api_view(["GET", "POST"])
def libro_list(request):
    if request.method == "GET":
        libros = Libro.objects.all()
        ser = LibroSerializer(libros, many=True)
        return Response(ser.data)
    if request.method == "POST":
        ser = LibroSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def libro_detail(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        ser = LibroSerializer(libro)
        return Response(ser.data)
    if request.method == "PUT":
        ser = LibroSerializer(libro, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
