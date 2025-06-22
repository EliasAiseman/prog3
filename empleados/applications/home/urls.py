from django.urls import path
from .views import Vistahome

urlpatterns= [

    path('',Vistahome.as_view(), name='home')


]