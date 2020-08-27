from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Curso, Carrera, Estudiante

# Create your views here.

def index(request):
    return render(request, 'index.html',{
        'Titulo':'Inicio',
    })

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {
        'cursos': cursos,
        'Titulo':'Cursos',
    })

def carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras.html', {
        'carreras':carreras,
        'Titulo':'Carreras',
    })

def consultas(request):
    return render(request, 'consultas.html', {
        'Titulo':'Consultas',
    })

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {
        'Titulo':'Estudiantes',
        'estudiantes':estudiantes,
    })

def eliminar_cursos(request, id):
    cursos = Curso.objects.get(pk=id)
    cursos.delete()
    return redirect('cursos')

def eliminar_carreras(request,id):
    carreras = Carrera.objects.get(pk=id)
    carreras.delete()
    return redirect("carreras")

def eliminar_estudiantes(request,id):
    estudiantes = Estudiante.objects.get(pk=id)
    estudiantes.delete()
    return redirect("estudiantes")

def agregar_carrera(request):
    return render(request, 'create_carrera.html')

def save_carrera(request):
    carreras = Carrera(
        idcarrera = request.GET["idcarrera"],
        nombre =request.GET["nombre"] ,
        nombrecorto = request.GET["nombrecorto"],
        fechafundacion = request.GET["fechafundacion"],
        estado = request.GET["estado"]
        
    )
    carreras.save()  
    return redirect("carreras")

def agregar_estudiante(request):
    return render(request, 'create_estudiante.html')

def save_estudiante(request):
    estudiantes = Estudiante(
        idestudiante = request.GET["idestudiante"],
        codigo = request.GET["codigo"],
        nombre = request.GET["nombre"],
        apellidos = request.GET["apellidos"],
        dni = request.GET["dni"],
        direccion = request.GET["direccion"],
        fechanacimiento = request.GET["fechanacimiento"],
        estado = request.GET["estado"]
    )
    estudiantes.save()
    return redirect("estudiantes")

def agregar_cursos(request):
    return render(request, 'create_cursos.html')

def save_cursos(request):
    cursos = Curso(
        idcurso = request.GET["idcurso"],
        codigo = request.GET["codigo"],
        nombre = request.GET["nombre"],
        horas = request.GET["horas"],
        creditos = request.GET["creditos"],
        estado = request.GET["estado"]

    )
    cursos.save()
    return redirect("cursos")

