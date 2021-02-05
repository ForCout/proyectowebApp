from django.contrib import admin
from.models import Proyectos
# Register your models here.


class servicio_admin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')


admin.site.register(Proyectos, servicio_admin)
