from ..serializers.product import ProductSerializer, ProductFilter, BrandSerializer, CategorySerializer
from ..models.product import Product, Brand, Category
from django.http import Http404
from django.db.models import Q
from django.db.models.functions import Lower
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductList(APIView):
    """
    List all Product
    """
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):
    """
    get product by id.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    



class ProductSearch(APIView):
    def post(self, request):
        search_query = request.data.get('query', '')
        if search_query:
            search_results = Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(brand__name__icontains=search_query)
            )

            search_results = search_results.order_by('name')
            serializer = ProductSerializer(search_results, many=True)
            print(f"Search results: {serializer.data}")
            return Response(serializer.data)
        else:
            return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)
