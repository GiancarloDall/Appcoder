from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre= models.CharField(max_length=40)
    camada = models.IntegerField()


class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    materia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Alumno(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
