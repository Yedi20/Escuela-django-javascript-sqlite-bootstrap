from os import curdir
from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages
# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, 'Cursos listados!!')
    return render(request, "gestionCursos.html", {"Cursos":  cursosListados}) #ahoa vamos a lista los cusos

def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    notas= request.POST['numNotas']
     
    
    curso = Curso.objects.create(
     codigo = codigo, nombre = nombre, notas = notas)

    return redirect('/')
def eliminacionCurso (request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)

    return render(request, "edicionCurso.html", {"Curso": curso})
def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    notas= request.POST['numNotas']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre 
    curso.notas= notas
    curso.save()
      
    return redirect('/')