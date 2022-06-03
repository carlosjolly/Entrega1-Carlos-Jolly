from django.http import HttpResponse
from django.shortcuts import render
from carlosblog.forms import trabajoForm, contactoForm
from django import forms
from .models import Trabajos, Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request):
    return render(request, 'post.html')

def trabajos(request):
    return render(request, 'trabajos.html')

def alta_trabajo(request):
    
    if request.method == "POST":

        miform = trabajoForm (request.POST)

        if miform.is_valid():

            datos = miform.cleaned_data

            trabajo = Trabajos (nombre=datos['nombre'], trabajo=datos['trabajo'])
            trabajo.save()
        return render (request, 'trabajos.html')
    return render(request, 'trabajos.html')
    
def alta_contacto(request):

    if request.method == "POST":

        secondform = contactoForm(request.POST)

        if secondform.is_valid():

            datos = secondform.cleaned_data

            contacto = Contact(nombre=datos['nombre'], email=datos['email'], telefono=datos['telefono'] )
            contacto.save()
        
        return render(request,'contact.html')
    return render(request,'contact.html')




def busquedaTrabajos(request):

    return render(request,'busquedaTrabajos.html')

def buscar(request):

    respuesta = f"Estoy buscando el trabajo de :{request.GET['trabajos']}"

    return HttpResponse(respuesta)




