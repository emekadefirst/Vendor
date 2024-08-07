# from django.db.models import Sum, Count
# from django.utils import timezone
# from datetime import timedelta
# import json
# from product.models import Product, Order, Payment

# def dashboard_callback(request, context):
#     # Basic counts
#     context.update({
#         "total_Product": Product.objects.count(),
#         "total_Payment": Payment.objects.count(),
#         "total_Order": Order.objects.count(),
#     })
    
#     last_7_days = timezone.now() - timedelta(days=7)

#     payments_last_7_days = Payment.objects.filter(created_at__gte=last_7_days)\
#         .values('created_at__date')\
#         .annotate(total_amount=Sum('amount'))\
#         .order_by('created_at__date')

#     context['payments_last_7_days'] = json.dumps(
#         [{'date': item['created_at__date'].isoformat(), 'amount': item['total_amount']} for item in payments_last_7_days]
#     )

#     orders_last_7_days = Order.objects.filter(created_at__gte=last_7_days)\
#         .values('created_at__date')\
#         .annotate(total_orders=Count('id'))\
#         .order_by('created_at__date')

#     context['orders_last_7_days'] = json.dumps(
#         [{'date': item['created_at__date'].isoformat(), 'total_orders': item['total_orders']} for item in orders_last_7_days]
#     )
