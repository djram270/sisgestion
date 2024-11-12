from django import forms
from .models import Competencia, ResultadoAprendizaje, Asignatura, Docente

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['descripcion', 'tipo', 'nivel']

class ResultadoAprendizajeForm(forms.ModelForm):
    class Meta:
        model = ResultadoAprendizaje
        fields = ['competencia', 'descripcion']

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'creditos', 'objetivos', 'semestre']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['tipo_identificacion', 'tipo_docente', 'nombres', 'apellidos', 'identificacion', 'titulo']
