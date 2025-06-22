from django.urls import path
from .views import VistaDepartamento

urlpatterns=[
    path('', VistaDepartamento.as_view(), name= 'departamento')



]