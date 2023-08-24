from django.shortcuts import render
from models import Tabla

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    tabla = Tabla.objects.all().values()
    return render(request, 'about.html', {'tabla': tabla})
