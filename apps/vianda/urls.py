from django.urls import path

from apps.usuario import views

app_name = 'vianda'
urlpatterns = [
    path('', views.crear_vianda, name="vianda")
 ]