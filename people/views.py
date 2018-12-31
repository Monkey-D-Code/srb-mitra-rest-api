from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.status import *

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from . models import *
from . serializers import *

# Create your views here.

class CustomerCreateList(APIView):

   
    def get(self , request):
        users = Customer.objects.all()
        serializer = CustomerSerializer(users , many=True)
        return Response(serializer.data , status=HTTP_200_OK)

    def post(self , request):
        info = request.data
        if info.keys() == {'first_name' , 'last_name' , 'username' , 'email' , 'phone_number' , 'password' ,'re-password'} :
            
            if info['password'] == info['re-password']:
                
                # create the User Model Entry
                user = User.objects.create(
                    first_name    =  info['first_name'],
                    last_name    =  info['last_name'],
                    username    =  info['username'],
                    email    =  info['email'],
                    
                )
                user.set_password(info['password'])
                user.save()
                serializer = UserSerializer(user)
                customer = Customer.objects.create(user=user , phone_number=info['phone_number'])
                customer_ser = CustomerSerializer(customer)
                customer.save()
                token = Token.objects.create(user=user)
                token.save()
                return Response(serializer.data , status=HTTP_200_OK)
            else:

                return Response({"Error !" : "Passwords does not match"} , status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error !"  : "INVALID DATA INPUT !"} , status=HTTP_404_NOT_FOUND)



class CustomerProfile(APIView):

    def get(self , request , pk):
        users = Customer.objects.filter(id=pk)
        serializer = CustomerSerializer(users , many=True)
        return Response(serializer.data , status=HTTP_200_OK)
    
    def put(self , request , pk):
        info = request.data
        if info.keys() == {'first_name' , 'last_name' , 'email' , 'phone_number'} :
            
            customer = Customer.objects.filter(id=pk)
            customer.update(phone_number = info['phone_number'])
            user_id = 0

            for c in customer:
                user_id = c.user.id

            User.objects.filter(id=user_id).update(
                first_name = info['first_name'],
                last_name  = info['last_name'],
                email      = info['email'],

                )
            
            
            serializer = CustomerSerializer(customer , many=True)
            return Response(serializer.data , status=HTTP_200_OK)

        else:

            return Response({"Error !"  : "INVALID DATA INPUT !"} , status=HTTP_404_NOT_FOUND)

    def delete(self , request , pk):
        return Response({"pk" : pk})



class CustomerAddressView(APIView):

    def get(self , request , pk):
        address = CustomerAddress.objects.filter(customer=pk)
        serializer = CustomerAddressSerializer(address , many=True)
        return Response(serializer.data , status=HTTP_200_OK)


    def put(self , request , pk):
        return Response({"pk" : pk , "data" : request.data})

    def delete(self , request , pk):
        return Response({"pk" : pk})