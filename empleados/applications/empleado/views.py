
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Vistaempleado(TemplateView):
    template_name=  'empleado/empleado.html'

class Reportempleado(TemplateView):
    template_name='empleado/template_pdf.html'