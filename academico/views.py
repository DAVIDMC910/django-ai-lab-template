from django.views.generic import ListView, DetailView
from .models import Programa, Curso, Estudiante

class ProgramaListView(ListView):
    model = Programa
    template_name = "academico/programa_list.html"
    context_object_name = "programas"

class ProgramaDetailView(DetailView):
    model = Programa
    template_name = "academico/programa_detail.html"
    context_object_name = "programa"

class CursoListView(ListView):
    model = Curso
    template_name = "academico/curso_list.html"
    context_object_name = "cursos"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "academico/curso_detail.html"
    context_object_name = "curso"

class EstudianteListView(ListView):
    model = Estudiante
    template_name = "academico/estudiante_list.html"
    context_object_name = "estudiantes"

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "academico/estudiante_detail.html"
    context_object_name = "estudiante"