from django.contrib import admin
from .models import Cliente


# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at","updated_at")
    search_fields = ("nombre","celular")
    list_display = ("id","nombre","celular","whatsapp","direccion","correo","genero")
    list_per_page = 10

admin.site.register(Cliente, ClienteAdmin)    

 


#configuracion del panel de gestion

title = "Gestión Más Móvil Repair"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
