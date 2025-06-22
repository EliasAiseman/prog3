from django.urls import path
from .views import Vistaempleado, Reportempleado

urlpatterns=[

    path('',Vistaempleado.as_view(), name='home empleado'),
    path('',Reportempleado.as_view(), name='reporte')

]