from django.shortcuts import render
from .models import Proyectos

def home(request):
    proyectos_visible = Proyectos.objects.all()  # Obtiene todos los proyectos

    # Si no hay proyectos, se envía None o un mensaje vacío
    if not proyectos_visible.exists():
        proyectos_visible = None  # También puedes enviar []

    return render(request, 'mi_app/index.html', {'proyectos_visible': proyectos_visible})
