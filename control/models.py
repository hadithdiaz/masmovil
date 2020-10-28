from django.db import models

# Create your models here.


class Control(models.Model):




    MEDIO= (
        ("Efectivo", "Efectivo"),
        ("Transferencia", "Transferencia"),
        ("Debe", "Debe"),
        
    )

    REPARADO = (
        ("Si", "Si"),
        ("No", "No"),
    )

    fecha_out = models.DateField(null=True,blank=True,verbose_name="Fecha Salida")
    reparado = models.CharField(max_length=2,blank=True,choices=REPARADO,verbose_name="Reparado")
    diagnostico = models.TextField(blank=True,null=True,verbose_name="Diagnostico")
    reparacion = models.TextField(blank=True,null=True,verbose_name="Reparacion")
    gasto = models.DecimalField(default= "0",max_digits=10, decimal_places=0)
    cobro = models.DecimalField(default= "0",max_digits=10, decimal_places=0)
    total = models.DecimalField(null=True, default= "0",max_digits=10, decimal_places=0)
    medio_pago = models.CharField(null=True, max_length=15, default= "Efectivo",choices=MEDIO)


    

    class Meta:
        verbose_name = "Control"
        verbose_name_plural = "Controls"
        ordering = ["-id"]

    def __str__(self):
        return self.diagnostico
