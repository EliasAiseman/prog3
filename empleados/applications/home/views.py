from django.shortcuts import render,redirect
from django.views.generic import TemplateView


# Create your views here.


class Vistahome(TemplateView):
    template_name= 'inicio/index.html'

