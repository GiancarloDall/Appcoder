from django.shortcuts import render
from Appcoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from Appcoder.forms import Curso_formulario

# Create your views here.
def inicio(request):
    return render( request , "padre.html")


def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=1243124)
    curso.save()
    texto = f"se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumnos(request):
    return render(request , "alumnos.html")



def curso_formulario(request):
    

    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

        curso = Curso( nombre=request.POST["nombre"] , camada=request.POST["camada"])
        curso.save()
        return render(request , "formulario.html")
    


    return render(request , "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request, "resultado_busqueda.html" , {"cursos":cursos})

    else:
        return HttpResponse("ingrese el nombre del curso")
        
     
     
     
     
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor, Alumno  # Importar sus modelos

# Vistas para Profesores

class ProfesorListView(ListView):
    model = Profesor  # Especificar el modelo a manejar
    template_name = 'profesor_list.html'  # Plantilla para mostrar profesores

class ProfesorCreateView(CreateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'materia']
    template_name = 'profesor_form.html'  # Plantilla para el formulario de creación
    success_url = '/profesores/'  # URL a la que redirigir después de una creación exitosa

class ProfesorUpdateView(UpdateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'materia']
    template_name = 'profesor_form.html'  # Plantilla para el formulario de edición
    success_url = '/profesores/'  # URL a la que redirigir después de una edición exitosa

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'profesor_confirm_delete.html'  # Plantilla para confirmación de eliminación
    success_url = '/profesores/'  # URL a la que redirigir después de una eliminación exitosa


# Vistas para Alumnos (similar a profesores)

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumno_list.html'

class AlumnoCreateView(CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'curso']
    template_name = 'alumno_form.html'
    success_url = '/alumnos/'

class AlumnoUpdateView(UpdateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'curso']
    template_name = 'alumno_form.html'
    success_url = '/alumnos/'

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumno_confirm_delete.html'
    success_url = '/alumnos/'