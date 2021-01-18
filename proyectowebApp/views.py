from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'proyectowebApp/home.html')


def contacto(request):
    return render(request, 'proyectowebApp/contacto.html')


def proyectos(request):
    return render(request, 'proyectowebApp/proyectos.html')


def blog(request):
    return render(request, 'proyectowebApp/blog.html')


def quiensoy(request):
    return render(request, 'proyectowebApp/quiensoy.html')
