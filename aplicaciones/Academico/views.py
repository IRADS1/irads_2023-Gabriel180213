from django.shortcuts import render, redirect
from . models import curso
from django.contrib import messages
# Create your views here.

def home(request):
    cursos = curso.objects.all()
    messages.success(request, '!CURSOS LISTADOS!')
    return render(request, "gestionCursos.html", {"cursos": cursos })

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    materia = curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request,codigo):
    curs = curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curs})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    cur = curso.objects.get(codigo=codigo)
    cur.nombre = nombre
    cur.creditos = creditos
    cur.save()

    return redirect('/')

def eliminarCurso(request,codigo):
    curs = curso.objects.get(codigo=codigo)
    curs.delete()

    return redirect('/')



