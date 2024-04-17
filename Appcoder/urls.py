from django.urls import path
from . import views 
from .views import (
    ProfesorListView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
    AlumnoListView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView
)

urlpatterns = [path('profesores/', ProfesorListView.as_view(), name='profesor_list'),
    path('profesores/crear/', ProfesorCreateView.as_view(), name='profesor_create'),
    path('profesores/editar/<int:pk>/', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/eliminar/<int:pk>/', ProfesorDeleteView.as_view(), name='profesor_delete'),

    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/crear/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/editar/<int:pk>/', AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/eliminar/<int:pk>/', AlumnoDeleteView.as_view(), name='alumno_delete'),

    path("", views.inicio, name="home"),
    path("ver_curso", views.ver_cursos , name="cursos"),
    # path("alta_curso/<nombre>",views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso",views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar)



]