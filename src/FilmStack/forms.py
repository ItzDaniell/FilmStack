from django import forms
from .models import Pelicula, Maraton

class MaratonForm(forms.ModelForm):
    class Meta:
        model = Maraton
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AgregarPeliculaForm(forms.Form):
    pelicula = forms.ModelChoiceField(
        queryset=Pelicula.objects.all(),
        label='Selecciona una película',
        widget=forms.Select(attrs={'class': 'form-control'})
    )