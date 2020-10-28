
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mainapp.forms import RegisterForm
from ordenes.models import Orden
from clientes.models import Cliente

# Create your views here.


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




def index(request):

    return render(request,"index.html",{
        "title": "Inicio"
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
    
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Te has registrado correctamente",)

            return redirect("inicio")



    return render(request,"users/register.html",{
        "title": "Registro",
        "register_form": register_form
    })

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")


        else: 
             messages.warning(request, "No te has identificado correctamente",)





    return render(request,"users/login.html",{
        "title": "Identificate"
    })



def logout_user(request):
    logout(request)

    return redirect("login")
    