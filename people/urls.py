from django.urls import *
from . views import *
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'people'

urlpatterns = [

    
    path('customer/all/' ,CustomerCreateList.as_view() , name='customer-signup'),
    
    path('customer/<pk>/profile/' , CustomerProfile.as_view() , name='customer-profile'),

    path('customer/<pk>/address/' , CustomerAddressView.as_view() , name='customer-address'),

    path('customer/login/' , obtain_auth_token , name='customer-login'),

    path('customer/info/' , CustomerFromToken.as_view() , name="token-to-customer"),

    
]
