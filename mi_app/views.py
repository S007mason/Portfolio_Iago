from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import Proyectos



from django.shortcuts import render
from .models import Proyectos

def home(request):
    proyectos = Proyectos.objects.all()
    offset = int(request.GET.get('offset', 0))  # Obtener el desplazamiento desde la URL, predeterminado a 0
    limit = 3  # Número de proyectos a mostrar por página

    proyectos_visible = proyectos[offset:offset + limit]  # Seleccionar el subconjunto de proyectos
    total_proyectos = proyectos.count()  # Contar todos los proyectos

    # Calcular si hay más elementos a la derecha o izquierda
    hay_anterior = offset > 0
    hay_siguiente = offset + limit < total_proyectos

    # Calcular los nuevos offsets
    offset_anterior = max(0, offset - limit)
    offset_siguiente = offset + limit

    return render(request, 'mi_app/index.html', {
        'proyectos_visible': proyectos_visible,
        'hay_anterior': hay_anterior,
        'hay_siguiente': hay_siguiente,
        'offset_anterior': offset_anterior,
        'offset_siguiente': offset_siguiente,
    })
