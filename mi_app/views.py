from django.shortcuts import render
from .models import Proyectos

def home(request):
    proyectos_visible = Proyectos.objects.all()  # Obtiene todos los proyectos
    return render(request, 'mi_app/index.html', {'proyectos_visible': proyectos_visible})
