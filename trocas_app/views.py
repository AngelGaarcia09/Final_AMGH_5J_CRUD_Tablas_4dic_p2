from pydoc import text
from django.shortcuts import render, redirect
from .models import Troca

# Create your views here.
def inicio_vistaTrocas(request):
    lastrocas = Troca.objects.all()
    return render(request, "gestionarTrocas.html", {"mistrocas": lastrocas})

def registrarTroca(request):
    id_troca = request.POST["txtcodigo"]
    año = request.POST["txtanio"]
    modelo = request.POST["txtmodelo"]
    marca = request.POST["txtmarca"]
    precio = request.POST["txtprecio"]
    color = request.POST["txtcolor"]
    tipo_llantas = request.POST["txtllantas"]
    id_sucursal =request.POST["txtcodigo"]

    Troca.objects.create(
        id_troca=id_troca,
        año=año,
        modelo=modelo,
        marca=marca,
        precio=precio,
        color=color,
        tipo_llantas=tipo_llantas,
        id_sucursal=id_sucursal
    )  # Guarda el registro

    return redirect("trocas")

def seleccionarTroca(request, codigo):
    troca = Troca.objects.get(id_troca=codigo)
    # troca = Troca.objects.get(id_sucursal=codigo)
    return render(request, "editarTroca.html", {"mistrocas": troca, "mistrocas": troca, "text": text})

def editarTroca(request):
    id_troca = request.POST["txtcodigo"]
    año = request.POST["txtanio"]
    modelo = request.POST["txtmodelo"]
    marca = request.POST["txtmarca"]
    precio = request.POST["txtprecio"]
    color = request.POST["txtcolor"]
    tipo_llantas = request.POST["txtllantas"]
    id_sucursal=request.POST["txtid_sucursal"]

    troca = Troca.objects.get(id_troca=id_troca)
    troca.año = año
    troca.modelo = modelo
    troca.marca = marca
    troca.precio = precio
    troca.color = color
    troca.tipo_llantas = tipo_llantas
    troca.id_sucursal = id_sucursal
    troca.save()  # Guarda el registro actualizado

    return redirect("trocas")

def borrarTroca(request, codigo):
    troca = Troca.objects.get(id_troca=codigo)
    troca.delete()  # Borra el registro
    return redirect("trocas")
