from django.contrib import admin
from .models import Control

# Register your models here.


class ControlAdmin(admin.ModelAdmin):
    #readonly_fields = ("created_at","updated_at")
    #search_fields = ("cliente","imei","marca","modelo","falla","accesorios")
    #search_fields = ('cliente__first_name', "imei")
    list_display = ("id","reparado","gasto")
    list_per_page = 10
admin.site.register(Control, ControlAdmin)   