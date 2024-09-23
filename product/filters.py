import django_filters
from .models import *
class ProductFilter(django_filters.FilterSet):
  name= django_filters.CharFilter(lookup_expr='iexact')
  Keyword = django_filters.filters.CharFilter(field_name='name',lookup_expr='icontains')
  minPrice = django_filters.filters.NumberFilter(field_name='price'or 0,lookup_expr='gte')

  class Meta:
    model = Product
    #fields=['category', 'brand']
    fields = ('category','brand','Keyword','minPrice')
    
