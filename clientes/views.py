from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Cliente
from ordenes.models import Orden
from .forms import FormCliente
from django.db.models import Q
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.views.generic import CreateView


# Create your views here.
 

@login_required(login_url="login")
def clientes(request):
    
    data = {
        "title": "Lista de Clientes",
        "clientes" : Cliente.objects.all()
        
        
    }
    
    return render(request,"clientes.html", data )



@login_required(login_url="login")
def crear_cliente(request):
    data= {
        "form": FormCliente()
    }

    if request.method == "POST":
        formulario = FormCliente(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
            return redirect("crear_orden")

    return render(request,"crear_cliente.html", data)


@login_required(login_url="login")
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    data= {
        "form": FormCliente(instance=cliente)
    }

    if request.method == "POST":
        formulario = FormCliente(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Editado Correctamente"
            data["form"]  =formulario
            return redirect("cliente", id=id)

    return render(request,"editar_cliente.html", data)   


@login_required(login_url="login")
def buscar(request):
    if request.method == "POST":
        buscar = request.POST["buscalo"]

        if buscar:
            clientes = Cliente.objects.filter(Q(nombre__contains=buscar) |
                                              Q(celular__contains=buscar)
                                              )
            if clientes:
                return render(request, "buscar.html", {"clientes": clientes})
            else:
                messages.error(request, "No encontrado")

        else:
            return redirect("clientes")

    return render(request, "buscar.html")




@login_required(login_url="login")
def cliente(request,id):
    data = { 
        "title": "Cliente",
        "cliente" : Cliente.objects.get(id=id)

    }
    return render(request,"cliente.html",data)    



    


