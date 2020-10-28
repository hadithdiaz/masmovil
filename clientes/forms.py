from django import forms
from django.forms import ModelForm
from .models import Cliente


class FormCliente(ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'celular',
            'whatsapp',
            'direccion',
            'correo',
            'genero',
            'status',

        ]
        labels = {
            'nombre': 'Nombre y Apellido',
            'celular': 'Numero Celular',
            'whatsapp': 'WhatsApp',
            'direccion': 'Dirección',
            'correo': 'E-mail',
            'genero': 'Genero',
            'status': 'Status',

        }

        widgets = {

            'nombre': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),
            'celular': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),

            'whatsapp': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),

            'direccion': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),  

            'correo': forms.EmailInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),   


            'genero': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),  
    
            'status': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),

        }





