from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class VistaDepartamento(TemplateView):
    template_name='departamento/departamento.html'