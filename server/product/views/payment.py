from pypstk.payment import Payment
from pypstk.status import Verify
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.payment import Payment

email = "customer@email.com"
amount = "20000"
secret_key = "your secret_key from api"

new_payment = Payment(email, amount, secret_key)
transaction_data = new_payment.initialize_transaction()
print(transaction_data)

class PaymentView(APIView):
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['user'].email
            amount = serializer.validated_data['amount']
            paystack = Paystack(email, amount, sk)
            payment_result = paystack.pay()
            # Construct a Response object with the payment result
            return Response(payment_result, status=rest_status.HTTP_200_OK)
        else:
            # If serializer is not valid, return a Response with serializer errors
            return Response(serializer.errors, status=rest_status.HTTP_400_BAD_REQUEST)
        
        

        

# Check webhook status
reference = "YOUR_REFERENCE"
secret_key = "YOUR_SECRET_KEY"

hook = Verify(reference, secret_key)
status = hook.status()
print(status)