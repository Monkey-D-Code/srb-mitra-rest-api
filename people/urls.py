from django.urls import *
from . views import *

app_name = 'people'

urlpatterns = [

    
    path('customer/all/' ,CustomerCreateList.as_view() , name='customer-signup'),
    
    path('customer/<pk>/profile/' , CustomerProfile.as_view() , name='customer-profile'),

    path('customer/<pk>/address/' , CustomerAddressView.as_view() , name='customer-address'),
]
