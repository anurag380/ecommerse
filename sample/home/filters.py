import django_filters
from .models import Products,Tag
from django import forms


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['category', 'tag']

    