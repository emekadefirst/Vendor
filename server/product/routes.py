from django.urls import path
from .views.product import *

urlpatterns = [
    path('search/', ProductSearch.as_view(), name='product-search'),
    path('all/', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]


