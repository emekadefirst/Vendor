from django.urls import path
from .views import LoginUser, RegisterUser, LogoutUser

urlpatterns = [
    path('login', LoginUser.as_view(), name='Login'),
    path('signup', RegisterUser.as_view(), name='Signup'),
    path('logout', LogoutUser.as_view(), name='Logout'),
]
