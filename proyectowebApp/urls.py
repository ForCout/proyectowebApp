from django.urls import path
from proyectowebApp import views

urlpatterns = [

    path("", views.home, name="Home"),
    path("contacto", views.contacto, name="Contacto"),
    path("blog", views.blog, name="Blog"),
    path("proyectos", views.proyectos, name="Proyectos"),
    path("quiensoy", views.quiensoy, name="Quien_soy"),

]

