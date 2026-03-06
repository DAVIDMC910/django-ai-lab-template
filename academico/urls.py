from django.urls import path
from .views import (
    ProgramaListView, ProgramaDetailView,
    CursoListView, CursoDetailView,
    EstudianteListView, EstudianteDetailView
)

app_name = "academico"

urlpatterns = [
    path("programas/", ProgramaListView.as_view(), name="programa_list"),
    path("programas/<int:pk>/", ProgramaDetailView.as_view(), name="programa_detail"),

    path("cursos/", CursoListView.as_view(), name="curso_list"),
    path("cursos/<int:pk>/", CursoDetailView.as_view(), name="curso_detail"),

    path("estudiantes/", EstudianteListView.as_view(), name="estudiante_list"),
    path("estudiantes/<int:pk>/", EstudianteDetailView.as_view(), name="estudiante_detail"),
]