from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [

    
    path("crear_orden/", views.CreateOrden.as_view(), name ="crear_orden"),
    path("ordenes/", views.Ordenes.as_view(), name = "ordenes"),
    path('editar_orden/<pk>/',views.EditarOrden.as_view(), name = "editar_orden"),
    path('orden/<pk>/',views.OrdenView.as_view(), name = "orden"),
    path('repair/<pk>/',views.Repair.as_view(), name = "repair"),
    path("tecnico", views.tecnico, name="tecnico"),
    path('tecnico_ver/<int:id>/',views.tecnico_ver, name = "tecnico_ver"),
    path('tecnico_edit/<pk>/',views.TecnicoEdit.as_view(), name = "tecnico_edit"),
    path('salida/<id>/',views.salida, name = "salida"),
    path('estado/<pk>/',views.EstadoEdit.as_view(), name = "estado"),
    path("balance", views.balance, name="balance"),



    

]