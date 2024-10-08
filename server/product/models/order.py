from django.db import models
from .action import CartItem
from django.contrib.auth.models import User
from datetime import datetime


def order_id():
    now = datetime.now()
    date_str = now.strftime('%Y%m%d')
    time_str = now.strftime('%H%M%S')
    return f'OD{date_str}{time_str}'


class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('en_route', 'En Route'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    id = models.AutoField(primary_key=True)
    order_code = models.CharField(max_length=15, default=order_id, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Order {self.order_code} - {self.user.username}"
    
    def total(self):
        return sum(item.subtotal() for item in self.items.all())
    
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)