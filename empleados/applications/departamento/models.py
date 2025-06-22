from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Departamento (models.Model):
  nombre= models.CharField('Nombre',max_length=50,blank=True)
  sigla= models.CharField('Sigla', max_length=30)
  activo= models.BooleanField('¿Está activo?', default=False)
  piso= models.CharField('Piso', max_length=5, blank=True)
  oficina = models.CharField('Oficina', max_length=10, blank=True)
  class Meta:
    verbose_name = 'Empresa'
    verbose_name_plural= 'Departamentos'
    ordering=['nombre']
    unique_together=('nombre','sigla')
  def __str__(self):
    return self.nombre + '-' + self.sigla + '-' + self.piso + '-' + self.oficina