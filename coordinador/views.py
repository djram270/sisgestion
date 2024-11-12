from django.shortcuts import render, redirect, get_object_or_404
from .models import Competencia, ResultadoAprendizaje, Asignatura, Docente
from .forms import CompetenciaForm, ResultadoAprendizajeForm, AsignaturaForm, DocenteForm


# Gestión de Competencias
def crear_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'coordinador/crear_competencia.html', {'form': form})

def listar_competencias(request):
    competencias = Competencia.objects.all()
    return render(request, 'coordinador/listar_competencias.html', {'competencias': competencias})

def editar_competencia(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('listar_competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'coordinador/editar_competencia.html', {'form': form})

# Gestión de Resultados de Aprendizaje
def crear_resultado_aprendizaje(request):
    if request.method == 'POST':
        form = ResultadoAprendizajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_resultados_aprendizaje')
    else:
        form = ResultadoAprendizajeForm()
    return render(request, 'coordinador/crear_resultado_aprendizaje.html', {'form': form})

def listar_resultados_aprendizaje(request):
    resultados = ResultadoAprendizaje.objects.all()
    return render(request, 'coordinador/listar_resultados_aprendizaje.html', {'resultados': resultados})

# Gestión de Asignaturas
def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'coordinador/crear_asignatura.html', {'form': form})

def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'coordinador/listar_asignaturas.html', {'asignaturas': asignaturas})



def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')  # Redirige después de guardar
    else:
        form = DocenteForm()
    
    # Asegúrate de retornar un objeto HttpResponse aquí
    return render(request, 'coordinador/crear_docente.html', {'form': form})




def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'coordinador/listar_docentes.html', {'docentes': docentes})
