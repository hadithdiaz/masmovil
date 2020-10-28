from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Orden
from .forms import OrdenForm, FormRepair, FormSalida
from .filters import OrdenFilter
from django.db import models
from django.views.generic.edit import (
    FormView
)
#
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView   
    )

# Create your views here.

class CreateOrden(CreateView):
    template_name = "crear_orden.html"
    model = Orden
    form_class = OrdenForm
    success_url = "/ordenes"

class Ordenes(ListView):
    template_name = "ordenes.html"
    queryset = Orden.objects.order_by('-id')
    #paginate_by = 4
    #ordering = "-id"
    model = Orden
    


class EditarOrden(UpdateView):
    template_name = "editar_orden.html"
    model = Orden
    fields = ('cliente', 'imei', 'modelo', 'contraseña', 'falla', 'accesorios', 'observacion', 'estado',)
    success_url = "/ordenes"



class OrdenView(DetailView):
    template_name = "orden.html"
    model = Orden




@login_required(login_url="login")
def home(request):
	ordenes = Orden.objects.all()
	clientes = Cliente.objects.all()

	total_clientes = clientes.count()

	total_ordenes = ordenes.filter(estado='En reparación').count()
	reparado = ordenes.filter(estado='Reparado').count()
	recibido = ordenes.filter(estado='Recibido').count()
    

	context = {'ordenes':ordenes, 'clientes':clientes,
    'total_ordenes':total_ordenes,'reparado':reparado,
	'recibido':recibido}

	return render(request, 'dashboard.html', context)



def buscar_orden(request):
    if request.method == "POST":
        buscar_orden = request.POST["buscalo"]

        if buscar_orden:
            ordenes = Orden.objects.filter(Q(imei__contains=buscar_orden) |
                                           Q(falla__contains=buscar_orden)
                                              )
            if ordenes:
                return render(request, "buscar_orden.html", {"ordenes": ordenes})
            else:
                messages.error(request, "No encontrado")

        else:
            return redirect("ordenes")

    return render(request, "buscar_orden.html")    



def salida(request, id):
    orden = Orden.objects.get(id=id)
    data= {
        "form": FormSalida(instance=orden)
    }

    if request.method == "POST":
        formulario = FormSalida(data=request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Editado Correctamente"
            data["form"]  =formulario
            return redirect("home")

    return render(request,"salida.html", data)




def repair(request, id):
    orden = Orden.objects.get(id=id)
    data= {
        "form": FormRepair(instance=orden)
    }

    if request.method == "POST":
        formulario = FormRepair(data=request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Editado Correctamente"
            data["form"]  =formulario
            return redirect("tecnico")

    return render(request,"repair.html", data)
    

"""
def estado(request, id):
    orden = Orden.objects.get(id=id)
    data= {
        "form": FormEstado(instance=orden)
    }

    if request.method == "POST":
        formulario = FormEstado(data=request.POST, instance=orden)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Editado Correctamente"
            data["form"]  =formulario

    return render(request,"estado.html", data)
"""




    
@login_required(login_url="login")
def tecnico(request):
    ordenes = Orden.objects.all()
    recibido = ordenes.filter(estado='Recibido').count()
    en_reparacion = ordenes.filter(estado='En reparación').count()
    garantia= ordenes.filter(estado='Garantía').count()

    context = {'ordenes':ordenes,"recibido":recibido, "en_reparacion":en_reparacion,
    "garantia":garantia,
    "title": "Ordenes Pendientes"}
   

    return render(request,"tecnico.html", context)


def tecnico_ver(request,id):
    data = { 
        "title": "Orden",
        "orden" : Orden.objects.get(id=id)

    }
    return render(request,"tecnico_ver.html",data)


class TecnicoEdit(UpdateView):
    template_name = "tecnico_edit.html"
    model = Orden
    fields = ('reparado','estado')
    success_url = "/tecnico"

class EstadoEdit(UpdateView):
    template_name = "tecnico_edit.html"
    model = Orden
    fields = ('estado',)
    success_url = "/ordenes"






class Repair(UpdateView):
    template_name = "repair.html"
    model = Orden
    fields = ('reparado','diagnostico','reparacion','gasto','estado')
    success_url = "/tecnico"




def balance(request):
    ordenes = Orden.objects.all()

    entregado = ordenes.filter(estado='Entregado').count()

    context = {'ordenes':ordenes,"entregado":entregado,
     "title": "Ingresos",}
   

    return render(request,"balance.html", context)