from django.shortcuts import render

from apps.vianda.models import Vianda


# Create your views here.

def crear_vianda(request):
    if request.method == 'POST':
        viandaForm = Vianda(request.POST, request.FILES)
        if Vianda.is_valid():
            viandaOb = Vianda.save(commit=True)
    else:
        viandaForm = Vianda()

    context = {
        'formulario': viandaForm
    }
    return render(request, 'vianda/crear_vianda.html', context)