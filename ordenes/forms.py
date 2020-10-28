from django import forms
from django.forms import ModelForm
from .models import Orden, Cliente



class OrdenForm(forms.ModelForm):
    
    class Meta:
        model = Orden
        fields = [

            'cliente', 'imei', 'modelo', 'contraseña', 'falla', 'accesorios', 'observacion',
            'estado',

        ]


        labels = {
           'cliente': 'Cliente', 'imei': 'Imei', 'modelo': 'Modelo', 'contraseña': 'Contraseña',
            'falla': 'Daño', 'accesorios': 'Accesorios', 'observacion': 'Observación',
            'estado': 'Estado',
            
        }

        widgets = {

            #'fecha_out': DateInput(),
            
            'imei': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),
            'contraseña': forms.TextInput(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),
            'cliente': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),    
            'modelo': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),  
            'accesorios': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),   

            'estado': forms.Select(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),  

            'falla': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm'
                    }
                ),


            'observacion': forms.Textarea(
				attrs={
					'class': 'form-control form-control-sm'
					}
				),      


        }

        

class DateInput(forms.DateInput):
    input_type = "date"




class FormRepair(ModelForm):

    class Meta:
        model = Orden
        
        fields = [
            'id',
            'reparado',           
            'diagnostico',
            'reparacion',
            'gasto',
            'estado',     

        ]

        labels = {
            'reparado': 'Reparado',
            'diagnostico': 'Diagnostico',
            'reparacion': 'Reparación',
            'gasto': 'Gasto $:',
            'estado': 'Estado',
            
        }


        widgets = {

            'fecha_out': DateInput(),

            

        }


class FormSalida(ModelForm):

    class Meta:
        model = Orden
        
        fields = [
            'fecha_out',           
            'cobro',
            'medio_pago',
            'estado',
                   
        ]

        labels = {
            'Fecha_out': 'Fecha de Entrega',
            'cobro': 'Cobro $:',
            'medio_pago': 'Medio de Pago',
            'estado': 'Estado',
            
        }


        widgets = {

            'fecha_out': DateInput(),    

        }

class FormControl(ModelForm):

    class Meta:
        model = Orden
        
        fields = [
            'fecha_out',           
            'gasto',
            'cobro',
            'total',
            'medio_pago',
            
                   
        ]

        labels = {
            'Fecha_out': 'Fecha de Entrega',
            'gasto': 'Gasto $:',
            'cobro': 'Cobro $:',
            'total': 'Total $:',
            'medio_pago': 'Medio de Pago',
            
        }


        widgets = {

            'fecha_out': DateInput(),    

        }
