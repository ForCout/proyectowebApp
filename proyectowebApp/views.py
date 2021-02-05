from django.shortcuts import render, HttpResponse
from proyectos.models import Proyectos


def home(request):
    return render(request, 'proyectowebApp/home.html')


def contacto(request):
    return render(request, 'proyectowebApp/contacto.html')


def proyectos(request):
    proyectos = Proyectos.objects.all()
    return render(request, "proyectowebApp/proyectos.html", {"proyectos": proyectos})


def blog(request):
    return render(request, 'proyectowebApp/blog.html')


def servicios(request):
    return render(request, 'proyectowebApp/servicios.html')
