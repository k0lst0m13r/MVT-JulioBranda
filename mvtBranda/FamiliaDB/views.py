from django.shortcuts import render, HttpResponse
from FamiliaDB.models import *

def index(request):
    
    familia = Familiar.objects.all()
    mascotas = Mascota.objects.all()  
    
    
    ctx = {"familia": familia, "mascotas": mascotas} 
    return render(request, 'FamiliaDB/index.html', ctx)
   