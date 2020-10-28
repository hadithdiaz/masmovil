from django.db import models
from clientes.choices import GENERO, STATUS


# Create your models here.


class Cliente(models.Model):


    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    celular = models.CharField(max_length=10, verbose_name="Numero Celular")
    whatsapp = models.CharField(blank=True,max_length=10, verbose_name="WhatsApp")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    correo = models.EmailField(blank=True,max_length=50, verbose_name="E-mail")
    genero = models.CharField(max_length=6, null=True,default= "hombre", choices=GENERO)
    status = models.CharField(max_length=7, null=True, default= "cliente", choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")


    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-id"]

    def __str__(self):
        return self.nombre

