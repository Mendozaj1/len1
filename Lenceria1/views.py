
from django.shortcuts import render, HttpResponse
from Lenceria1.models import *

# Create your views here.
#Paguina principal
def index(request):
    return render(request, 'index.html', {
    })
    
#Categoria
def Productos(request):
    articulos = Articulo.objects.all()      

    return render(request, 'Productos.html', {
        'articulos': articulos
    })
# Contactos
def contacto(request):
    return render(request, 'contacto.html')

#Borrar producto x la base de datos 
def borrar(request, id):
    articulos = Articulo.objects.get(pk = id)
    articulos.delete()

#  Ctegorias menus desplegables 
def jugetes(request):
    jugete = Jugetes.objects.all()

    return render(request, 'Jugete.html', {
        'jugete': jugete
    })

def lenceria_mujer(request):
    len_mujer = Lenceria_Mujeres.objects.all()

    return render(request, 'lenceria_mujer.html', {
        'len_mujer': len_mujer
    })

def lenceria_hombre(request):
    len_hombre = Lenceria_Hombres.objects.all()

    return render(request, 'lenceria_h.html', {
        'len_hombre': len_hombre
    })

def lubricante_cosmeticos(request):
    lubricante_cosmetico = Lubricante_cosmeticos.objects.all()

    return render(request, 'lubricante_cosmeticos.html', {
        'lubricante_cosmetico': lubricante_cosmetico
    })

def despedida_soltera(request):
    soltera = Despedida_soltera.objects.all()

    return render(request, 'despedida_soltera.html',{
        'soltera': soltera
    })
    
