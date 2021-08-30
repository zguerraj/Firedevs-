from gestionEstudiantes.forms import estudianteForms, grupoForms
from gestionEstudiantes.models import Estudiantes, Grupos
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import date
# Create your views here.


def home(request): 
    return render(request, 'gestionEstudiantes/home.html')

def listadoEstudiante(request):
    data = {
        'listaE' : Estudiantes.objects.all()
    }
    return render(request, 'gestionEstudiantes/listado_estudiante.html', data)

def listadoGrupo(request):
    data = {
        'listaG': Grupos.objects.all()
    }
    return render(request, 'gestionEstudiantes/listado_grupo.html', data)



def addGrupo(request):
    data = {
        'form': grupoForms()
    }

    if request.method == 'POST':
        form_aux = grupoForms(request.POST)
        if form_aux.is_valid():
            form_aux.save()
            messages.success(request, "Grupo registrado")
        else:
            messages.error(request, "Grupo no registrado, datos incorrectos")
            
    return render(request, 'gestionEstudiantes/agregar_grupo.html', data)

def calcular_años(fecha_naciento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_naciento.year
    # esta re asicnacion a resultado nos comprueba la edad exacta contando los meses
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_naciento.month, fecha_naciento.day))
    return resultado


def addEstudiante(request):
    data = {
        'form': estudianteForms()
    }
    listaGrupo=Grupos.objects.all()   

    if not listaGrupo:
        messages.warning(request, "Debe registrar un grupo")
        return redirect(to='home')

    if request.method == 'POST':
        form_aux = estudianteForms(request.POST)
        if form_aux.is_valid():
            email = form_aux.cleaned_data['email']
            edad = form_aux.cleaned_data['edad']
            fecha = form_aux.cleaned_data['fechaNacimiento']
            edadCalculada = calcular_años(fecha)
            if edadCalculada != edad or edad < 18 or edad > 90 or Estudiantes.objects.filter(email=email).exists():
                messages.error(request, "Estudiante no registrado, datos incorrectos")
            else:
                form_aux.save()
                messages.success(request, "Estudiante regisrado")
        else:
            messages.error(request, "Estudiante no registrado, datos incorrectos")
            
    return render(request, 'gestionEstudiantes/agregar_estudiante.html', data)

def eliminarGrupo(request, id):
    grupo=Grupos.objects.get(id=id)
    grupo.delete()
    messages.success(request, "Grupo eliminado corectamente")
    
    return redirect(to='Lista_Grupos')


def modificarEstudiante(request, id):
    est = Estudiantes.objects.get(id=id)
    data = {
        'form': estudianteForms(instance=est)
    }

    if request.method == 'POST' and 'submit' in request.POST:
        form_aux = estudianteForms(data=request.POST, instance=est)
        if form_aux.is_valid:
            form_aux.save()
            messages.success(request, "Estudiante modificado correctamente")
            data['form'] = form_aux

    if request.method == 'POST' and 'submit1' in request.POST:
        return redirect(to='Lista_Estudiantes')
        
    return render(request, 'gestionEstudiantes/modificar_estudiante.html', data)

def modificarGrupo(request, id):
    grupo = Grupos.objects.get(id=id)
    data = {
        'form': grupoForms(instance=grupo)
    }

    if request.method == 'POST' and 'submit' in request.POST:
        form_aux = grupoForms(data=request.POST, instance=grupo)
        if form_aux.is_valid:
            form_aux.save()
            messages.success(request, "Grupo modificado correctamente")
            data['form'] = form_aux

    if request.method == 'POST' and 'submit1' in request.POST:
        return redirect(to='Lista_Grupos')
        
    return render(request, 'gestionEstudiantes/modificar_grupo.html', data)

def eliminarEstudiante(request, id):
    est=Estudiantes.objects.get(id=id)
    est.delete()
    messages.success(request, "Estudiante eliminado corectamente")

    return redirect(to='Lista_Estudiantes')
