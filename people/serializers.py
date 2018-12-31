from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User



class UserSerializer(ModelSerializer):


    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {"password" : {"write_only" : True }}






class CustomerSerializer(ModelSerializer):

    user = UserSerializer(required=True)
    
    class Meta:
        model = Customer
        fields = ('id', 'user' , 'phone_number')
    
    
class CustomerAddressSerializer(ModelSerializer):
    
    class Meta:
        model = CustomerAddress
        fields = '__all__'
        



   



class DeliveryPersonSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'