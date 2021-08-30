from django import forms
from django.forms import ModelForm
from gestionEstudiantes.models import Estudiantes, Grupos

class grupoForms(ModelForm):
    class Meta:
        model = Grupos        
        fields = ['nombre', 'profesorGuia']
        labels = { 'nombre': ('Nombre:'), 'profesorGuia': ('Profesor Guía:')}
        

class estudianteForms(ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'edad', 'fechaNacimiento', 'ciudadNacimiento', 'sexo', 'email', 'grupo']
        labels = { 'nombre': ('Nombre:'), 'edad': ('Edad:'), 'fechaNacimiento': ('Fecha de Nacimiento:'), 'ciudadNacimiento': ('Ciudad de Nacimiento:'), 'sexo': ('Sexo:'), 'email': ('Email:'), 'grupo': ('Grupo:')}
        widgets = {'sexo': forms.RadioSelect(choices=[
            (True, 'Femenino'),
            (False, 'Masculino')             
        ]), 'fechaNacimiento': forms.DateInput(attrs={'type':'date'})}
      
