from django.db import models
from aplicaciones.departamento.models import Departamento
# Create your models here.
class Habilidades (models.Model):
  Habilidad=models.CharField('Habilidad', max_length=50)

  class Meta:
    verbose_name='Habilidad'
    verbose_name_plural='Habilidades del empleado'
    ordering=['habilidad']
    unique_together= ('habilidad','departamento')
  def __str__(self):
    return self.habilidad



class Empleado(models.Model):
  Trabajos=(
  ('0','contador'),('1','Administrativo'),('2','Desarrollador'),('3','Analista'),

          )


  nombre=models.CharField('Nombre', max_length=50)
  apellido=models.CharField('Apellido', max_length=50)
  ocupacion= models.CharField('Puesto', max_length=1,choices=Trabajos)
  Departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE)
  habilidades= models.ManyToManyField(Habilidades)
class Meta:
  verbose_name='Empleado'
  verbose_name_plural='Empleados empresa'
  ordering=['nombre','apellido']
  unique_together=('nombre','departamento')


def __str__(self):
  return self.nombre + '-' + self.apellido + '-' + self.piso + '-' + self.oficina
