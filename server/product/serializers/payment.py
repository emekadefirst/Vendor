from rest_framework import serializers
from order import OrderSerializer
from models.payment import Payment
from models.order import Order

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        order_data = validated_data.pop('order')
        order = Order.objects.create(**order_data)
        payment = Payment.objects.create(order=order, **validated_data)
        return payment


