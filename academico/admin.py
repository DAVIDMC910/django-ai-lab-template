from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion

admin.site.register(Programa)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)