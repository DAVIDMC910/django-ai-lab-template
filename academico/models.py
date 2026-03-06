from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="cursos")
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nombre} ({self.programa.nombre})"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} <{self.email}>"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripciones")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["estudiante", "curso"], name="unique_estudiante_curso")
        ]

    def __str__(self):
        return f"{self.estudiante.nombre} -> {self.curso.nombre}"