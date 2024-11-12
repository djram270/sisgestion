from django.urls import path
from . import views

urlpatterns = [
    path('crear_competencia/', views.crear_competencia, name='crear_competencia'),
    path('listar_competencias/', views.listar_competencias, name='listar_competencias'),
    path('editar_competencia/<int:pk>/', views.editar_competencia, name='editar_competencia'),
    path('crear_resultado_aprendizaje/', views.crear_resultado_aprendizaje, name='crear_resultado_aprendizaje'),
    path('listar_resultados_aprendizaje/', views.listar_resultados_aprendizaje, name='listar_resultados_aprendizaje'),
    path('crear_asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('listar_asignaturas/', views.listar_asignaturas, name='listar_asignaturas'),
    path('crear_docente/', views.crear_docente, name='crear_docente'),
    path('listar_docentes/', views.listar_docentes, name='listar_docentes'),  # Asegúrate de que listar_docentes existe en views.py
]

