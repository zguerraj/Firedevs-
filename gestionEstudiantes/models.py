from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE

# Create your models here.

profesor_status = [
    ('Profesor 1', 'Profesor 1'),
    ('Profesor 2', 'Profesor 2'),
    ('Profesor 3', 'Profesor 3'),
    ('Profesor 4', 'Profesor 4'),
    ('Profesor 5', 'Profesor 5')
]

ciudad_status = [
    ('Ciudad 1', 'Ciudad 1'),
    ('Ciudad 2', 'Ciudad 2'),
    ('Ciudad 3', 'Ciudad 3'),
    ('Ciudad 4', 'Ciudad 4'),
    ('Ciudad 5', 'Ciudad 5')
]

class Grupos(models.Model):
    nombre=models.CharField(max_length=50)
    profesorGuia=models.CharField(max_length=50, choices=profesor_status)
    
    def __str__(self) -> str:
        return self.nombre

class Estudiantes(models.Model):
    edad=models.IntegerField()
    sexo=models.BooleanField()
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    fechaNacimiento=models.DateField()
    ciudadNacimiento=models.CharField(max_length=50, choices=ciudad_status)
    grupo=models.ForeignKey(Grupos, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.nombre

    def clean_email(self):
        email = self.cleaned_data['email']
        if Estudiantes.objects.filter(email=email).exists():
            raise ValidationError('El buzón ya existe')
        return email

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad < 18 and edad > 90:
            raise ValidationError('Edad incorrecta')
        return edad

