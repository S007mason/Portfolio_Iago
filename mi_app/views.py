from django.shortcuts import render  # Reemplaza la importación de HttpResponse

def home(request):
    return render(request, 'mi_app/index.html')  # Renderiza la plantilla