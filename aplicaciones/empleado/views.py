from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class Vistas (TemplateView):
  template_name= 'empleado/home.html'

class Lista(ListView):
  template_name= 'empleado/lista.html'
  queryset=['Elias','Aiseman','Analista De Sistemas']
  context_object_name= 'lista'


