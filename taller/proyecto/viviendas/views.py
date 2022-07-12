from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.
from viviendas.models import *

# importar los formularios de forms.py
from viviendas.forms import *

# Create your views here.

def index(request):

    edificio = Edificio.objects.all()

    informacion_template = {'edificio': edificio}
    return render(request, 'index.html', informacion_template)


def obtener_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)

    informacion_template = {'edificio': edificio}
    return render(request, 'obtenerEdificio.html', informacion_template)


def crear_edificio(request):
    """
    """
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)


def editar_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)


def crear_departamento(request):

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)


def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'crearDepartamento.html', diccionario)


def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)


def crear_departamento_edificio(request, id):
    """
    """
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crearDepartamentoEdificio.html', diccionario)
