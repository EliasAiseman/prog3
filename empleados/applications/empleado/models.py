from django.db import models
from applications.departamento.models import Departamento

class Trabajo(models.Model):
    nombre = models.CharField('Puesto de trabajo', max_length=100)
    descripcion = models.TextField('descripcion', blank=True, null=True)

    class Meta:
        verbose_name = 'Puesto de Trabajo'
        verbose_name_plural = 'Puestos de Trabajo'
        ordering = ['nombre']


    
    def __str__(self):
        return self.nombre
class Pais (models.Model):
    nombre = models.CharField('Pais', max_length=50, unique=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Empleado(models.Model):




    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
  
    trabajo = models.ForeignKey(Trabajo, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
  

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        return self.nombre_completo()

