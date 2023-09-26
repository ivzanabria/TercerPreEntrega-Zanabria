from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import (
    CursoFormulario,
    ProfesorFormulario,
    EstudiantesForm,
    EntregableForm,
    BuscarForms,
)

# Create your views here.


def curso(request):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def estudiantes(request):
    formulario = None
    print(f"{request.POST}")
    if request.method == "POST":
        # Si se ha enviado un formulario
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            # Realiza acciones con los datos del formulario
            Estudiante.objects.create(**formulario.cleaned_data)
        else:
            # Si es una solicitud GET, crea una instancia del formulario vacío
            formulario = EstudiantesForm()

    return render(request, "AppCoder/estudiantes.html", {"formulario": formulario})


def entregables(request):
    formulario = None
    print(f"{request.POST}")
    if request.method == "POST":
        # Si se ha enviado un formulario
        formulario = EntregableForm(request.POST)
        if formulario.is_valid():
            entregado = False
            if formulario.cleaned_data.get("entregado"):
                entregado = True
            formulario.cleaned_data.update({"entregado": entregado})
            # Realiza acciones con los datos del formulario
            Entregable.objects.create(**formulario.cleaned_data)
        else:
            # Si es una solicitud GET, crea una instancia del formulario vacío
            formulario = EntregableForm()

    return render(request, "AppCoder/entregables.html")


def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(
            request.POST
        )  # aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()

            return render(
                request, "AppCoder/inicio.html"
            )  # Vuelvo al inicio o a donde quieran

    else:
        miFormulario = CursoFormulario()  # Formulario vacio para construir el html

    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(
            request.POST
        )  # aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            profesor = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"],
            )

            profesor.save()

            return render(
                request, "AppCoder/inicio.html"
            )  # Vuelvo al inicio o a donde quieran

    else:
        miFormulario = ProfesorFormulario()  # Formulario vacio para construir el html

    return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})


def buscar(request):
    print(f"función buscar {request.GET}")
    nombre = request.GET.get("nombre")
    if nombre:
        # respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        alumnos = Estudiante.objects.filter(nombre__icontains=nombre)
        if alumnos:
            return render(request, "AppCoder/buscar.html", {"alumnos": alumnos})

    return render(request, "AppCoder/buscar.html", {"mensaje": "Alumno no encontrado"})
    # No olvidar from django.http import HttpResponse
    # return HttpResponse(respuesta)
