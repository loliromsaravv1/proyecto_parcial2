from django.forms import forms, DateInput

from apps import vianda


class SolicitudViandaForm(forms.ModelForm):
    class Meta:
        model = vianda
        fields = ('usuario', 'fechaInicioVianda', 'estado', 'platos', 'cantidadViandas', 'frecuencia')

        widgets = {
            'fechaInicioVianda': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

        }