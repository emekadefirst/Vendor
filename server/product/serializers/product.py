import django_filters
from rest_framework import serializers
from ..models.product import Product, Brand, Category

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
        


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price_min', 'price_max', 'brand', 'category']
