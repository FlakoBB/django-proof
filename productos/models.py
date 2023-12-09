from django.db import models

class Producto(models.Model):
  nombre = models.CharField(max_length=100, help_text='Nombre del producto')
  precio = models.IntegerField(help_text='Precio unitario')
  descripcion = models.CharField(max_length=200, help_text='Descripción')

  def __str__(self):
    return self.nombre
