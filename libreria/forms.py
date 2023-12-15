from django import forms
from datetime import date
from libreria.models import Libro


class RegistroLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
    titulo = forms.CharField()
    idioma = forms.CharField()
    fecha_publicacion = forms.DateField(widget=forms.DateInput)
    portada = forms.ImageField()

    titulo.widget.attrs['class']='form-control'
    idioma.widget.attrs['class']='form-control'
    fecha_publicacion.widget.attrs['class']='form-control'
    portada.widget.attrs['class']='form-control'