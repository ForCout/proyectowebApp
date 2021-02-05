from django.urls import path
from proyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.home, name="Home"),
    path("contacto", views.contacto, name="Contacto"),
    path("blog", views.blog, name="Blog"),
    path("proyectos", views.proyectos, name="Proyectos"),
    path("servicios", views.servicios, name="Servicios"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
