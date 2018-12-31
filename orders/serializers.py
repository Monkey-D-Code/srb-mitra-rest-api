from rest_framework.serializers import ModelSerializer
from .models import *


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class PurchaseSerializer(ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
