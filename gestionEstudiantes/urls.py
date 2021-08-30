from django.urls import path
from gestionEstudiantes.views import addEstudiante, addGrupo, eliminarEstudiante, eliminarGrupo, home, listadoEstudiante, listadoGrupo, modificarEstudiante, modificarGrupo

urlpatterns = [
    path('', home, name="home"),
    path('modificar_estudiante/<id>/', modificarEstudiante, name="Modificar_Estudiante"),
    path('modificar_grupo/<id>', modificarGrupo, name = "Modificar_Grupo"),
    path('eliminar_estudiante/<id>/', eliminarEstudiante, name="Eliminar_Estudiante"),
    path('eliminar_grupo/<id>/', eliminarGrupo, name="Eliminar_Grupo"),
    path('add_grupo/', addGrupo, name="Add_Grupo"),
    path('add_estudiante/', addEstudiante, name="Add_Estudiante"),
    path('listado_estudiantes/', listadoEstudiante, name="Lista_Estudiantes"),
    path('listado_grupos/', listadoGrupo, name="Lista_Grupos"),
]