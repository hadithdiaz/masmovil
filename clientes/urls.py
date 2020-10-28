from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [

    
    path("clientes/", views.clientes, name="clientes"),
    path("crear_cliente/", views.crear_cliente, name ="crear_cliente"),
    url(r'^buscar/$',views.buscar, name ="buscar"),
    path('editar_cliente/<id>/',views.editar_cliente, name = "editar"),
    path('cliente/<int:id>/',views.cliente, name = "cliente"),

    

    

]