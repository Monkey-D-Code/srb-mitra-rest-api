from django.urls import path
from .views import *
app_name = 'orders'

urlpatterns = [
    
    path('all/' , AllOrdersView().as_view() , name="all"),

    path('<customer_id>/carts/' , CartView.as_view() , name='customer-carts'),

    path('cart/<cart_id>/' , CartEditDeleteView.as_view() , name='edit-cart'),

    path('cart/<cart_id>/purchases/' , PurchaseAllView.as_view() , name='cart-items'),

    path('purchase/<purchase_id>/edit/' , PurchaseEditDeleteView.as_view() , name ='edit-purchase'),

    path('<cart_id>/orders/' , CustomerAllOrdersView.as_view() , name = 'all-orders'),

    path('<order_id>/edit/' , OrderEditDeleteView.as_view() , name='edit-order'),
]
