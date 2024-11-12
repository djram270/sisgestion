from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'coordinador/home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coordinador/', include('coordinador.urls')),
    path('', home, name='home'),  # Página de inicio
]
