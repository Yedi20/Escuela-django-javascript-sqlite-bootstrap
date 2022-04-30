from django import views
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home),
    path('registroCurso/', views.registroCurso),
    path('eliminacionCurso/<codigo>', views.eliminacionCurso),
    path('editarCurso/', views.editarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso)
    
]