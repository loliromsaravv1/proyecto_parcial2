from django.db import models
from django.db.models import Choices, Count


# Create your models here.


class Plato(models.Model):
    objects = None
    descripcionPlato = models.CharField(max_length=200)
    activo = models.BooleanField()


class Vianda(models.Model):
    usuario = models.ForeignKey("usuario.user.username", on_delete=models.CASCADE, null=True)
    fechaInicioVianda = models.DateField()
    ESTADO_OPCIONES = (
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado')
    )
    estado = models.CharField(max_length=9, choices=ESTADO_OPCIONES)
    platos = models.ManyToManyField(Plato)
    cantidadViandas = Plato.objects.values("contest").annotate(Count("id"))
    FRECUENCIA_OPCIONES = (
        ('semanal', 'Semanal'),
        ('quincenal', 'Quincenal')
    )
    frecuencia = models.CharField(max_length=9, choices=FRECUENCIA_OPCIONES)
