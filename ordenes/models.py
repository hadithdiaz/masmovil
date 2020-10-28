from django.db import models
from django.forms import model_to_dict
from clientes.models import Cliente
from ordenes.choices import MEDIO_PAGO, REPARADO, ESTADO, MODELOS, ACSS

# Create your models here.


class Orden(models.Model):


    cliente = models.ForeignKey(Cliente, null=True, verbose_name="Cliente", blank=False, on_delete=models.PROTECT)
    imei = models.CharField(max_length=15,blank=True, verbose_name="Imei")
    modelo = models.CharField(max_length=20, null=True, choices=MODELOS, verbose_name="Modelo")
    contraseña = models.CharField(max_length=6,null=True,blank=True,verbose_name="Contraseña")
    falla = models.TextField(blank=False,null=True,verbose_name="Falla")
    accesorios = models.CharField(max_length=2, blank=True, null=True, choices=ACSS)
    observacion = models.TextField(blank=True,null=True,verbose_name="Observación")
    estado = models.CharField(max_length=15, default= "Recibido",choices=ESTADO)
    fecha_out = models.DateField(null=True,blank=True,verbose_name="Fecha Salida")
    reparado = models.CharField(max_length=2,blank=True,choices=REPARADO,verbose_name="Reparado")
    diagnostico = models.TextField(blank=True,null=True,verbose_name="Diagnostico")
    reparacion = models.TextField(blank=True,null=True,verbose_name="Reparacion")
    gasto = models.DecimalField(default= "0",max_digits=10, decimal_places=0)
    cobro = models.DecimalField(default= "0",max_digits=10, decimal_places=0)
    total = models.DecimalField(null=True, default= "0",max_digits=10, decimal_places=0)
    medio_pago = models.CharField(null=True, max_length=15, default= "Efectivo",choices=MEDIO_PAGO)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el") 
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")
   

    def toJSON(self):
        item = model_to_dict(self)
        item['gasto'] = format(self.gasto, '.2f')
        item['cobro'] = format(self.cobro, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha_out'] = self.fecha_out.strftime('%Y-%m-%d')
        return item


    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        ordering = ["-id"]

    def __str__(self):
        return self.imei



