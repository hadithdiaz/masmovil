import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrdenFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="created_at", lookup_expr='gte')
	end_date = DateFilter(field_name="created_at", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Orden
		fields = '__all__'
		exclude = ['cliente', 'created_at']