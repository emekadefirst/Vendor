from django.contrib import admin
from unfold.admin import ModelAdmin
from .models.action import Cart, CartItem
from .models.order import Order
from .models.payment import Payment
from .models.product import Category, Brand, Product, ProductImage, ProductRating
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
admin.autodiscover()

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductRatingInline(admin.TabularInline):
    model = ProductRating
    extra = 0
    readonly_fields = ('product', 'rating', 'comment')

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name', 'category', 'brand', 'price', 'stock_quantity', 'average_rating', 'created_at']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline, ProductRatingInline]
    readonly_fields = ('created_at', 'updated_at', 'average_rating')

@admin.register(CartItem)
class CartItemAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['user', 'product', 'quantity', 'subtotal']
    list_filter = ['user']
    search_fields = ['user__username', 'product__name']
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm  

@admin.register(Cart)
class CartAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['user', 'total']
    search_fields = ['user__username']
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm  

@admin.register(Order)
class OrderAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['order_code', 'user', 'status', 'created_at', 'total']
    list_filter = ['status', 'created_at']
    search_fields = ['order_code', 'user__username']
    readonly_fields = ['order_code', 'created_at']
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm  

@admin.register(Payment)
class PaymentAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['order', 'status', 'reference_id']
    list_filter = ['status']
    search_fields = ['order__order_code', 'reference_id']
    import_form_class = ImportForm
    export_form_class = SelectableFieldsExportForm  


