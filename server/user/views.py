from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.models.action import Cart
from product.serializers.actions import CartSerializer
from product.models.order import Order, Transaction
from product.serializers.order import OrderSerializer, TransactionSerializer
from django.contrib.auth import login
from .serializers import UserSignupSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.account.utils import complete_signup
from django.core.exceptions import ObjectDoesNotExist

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
            login(request, user, backend=user.backend)
            complete_signup(request._request, user, None, 'optional')

            refresh = RefreshToken.for_user(user)
            user_data = {
                'username': user.username,
                'email': user.email,
                'id': user.id,
            }
            return Response({
                'message': 'Registration successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)

            refresh = RefreshToken.for_user(user)
            user_data = {
                'username': user.username,
                'email': user.email,
                'id': user.id,
            }

            user_cart_data = None
            user_order_data = None
            user_transaction_data = None

            try:
                # User cart
                user_cart = Cart.objects.get(user=user)
                user_cart_data = CartSerializer(user_cart).data
                user_cart_data.update({'user': user_data})
            except ObjectDoesNotExist:
                pass  

            try:
                # User order
                user_order = Order.objects.get(user=user)
                user_order_data = OrderSerializer(user_order).data
                user_order_data.update({'user': user_data})
            except ObjectDoesNotExist:
                pass  

            try:
                # User transaction
                user_transaction = Transaction.objects.get(user=user)
                user_transaction_data = TransactionSerializer(user_transaction).data
                user_transaction_data.update({'user': user_data})
            except ObjectDoesNotExist:
                pass  

            return Response({
                'message': 'Login successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data,
                'cart': user_cart_data,
                'order': user_order_data,
                'transaction': user_transaction_data,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
