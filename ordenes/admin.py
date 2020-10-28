from django.contrib import admin
from .models import Orden

# Register your models here.


class OrdenAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at","updated_at")
    #search_fields = ("cliente","imei","marca","modelo","falla","accesorios")
    search_fields = ('cliente__first_name', "imei")
    list_display = ("id","cliente","imei","modelo","falla","accesorios")
    list_per_page = 10
admin.site.register(Orden, OrdenAdmin)   