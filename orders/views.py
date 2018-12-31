from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.status import *

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from . models import *
from . serializers import *
from people.models import *
from products.models import *
# Create your views here.
class AllOrdersView(APIView):

    def get(self,request):

        orders = Order.objects.all()
        serializer = OrderSerializer(orders , many=True)
        return Response(serializer.data , status=HTTP_200_OK)


class CartView(APIView):

    def get(self , request , customer_id):

        cart = Cart.objects.filter(customer=customer_id)
        serializer = CartSerializer(cart , many=True)
        return Response(serializer.data , status=HTTP_200_OK)

    def post(self , request , customer_id):

        customer = Customer.objects.filter(id=customer_id).first()

        cart = Cart.objects.create(

            customer = customer,
            status = 'S',
        )
        
        cart_1 = Cart.objects.filter(customer=customer_id)
        serializer = CartSerializer(cart_1 , many=True)
        return Response(serializer.data , status=HTTP_201_CREATED)

    
class CartEditDeleteView(APIView):

    def get(self , request , cart_id):
        
        carts = Cart.objects.filter(id=cart_id)
        serializer = CartSerializer(carts , many=True)
        return Response(serializer.data , status=HTTP_200_OK)

    def put(self , request , cart_id):
        info = request.data
        if info.keys() == {"status"} :

            cart = Cart.objects.filter(id=cart_id)
            cart.update(status=info['status'])
            serializer = CartSerializer(cart , many=True)
            return Response(serializer.data ,  status=HTTP_201_CREATED)

        else:

           return Response({"Error !"  : "INVALID DATA INPUT !"} , status=HTTP_404_NOT_FOUND) 
        
    def delete(self , request , cart_id):

        if Cart.objects.filter(id=cart_id).delete():
            return Response({"Success !" : "Cart "+str(cart_id)+" Deleted"} , status=HTTP_202_ACCEPTED)
        else:
            return Response({"Error !" : "Cart "+str(cart_id)+" Delete Failed !"} , status=HTTP_404_NOT_FOUND)


class PurchaseAllView(APIView):

    def get(self , request , cart_id):

        purchases = Purchase.objects.filter(cart=cart_id)
        serializer = PurchaseSerializer(purchases , many=True)
        return Response(serializer.data , status=HTTP_200_OK)

    def post(self , request , cart_id):

        info=request.data
        
        if info.keys() == {'quantity' , 'product'}:
            
            cart = Cart.objects.filter(id=cart_id).first()
            product = Product.objects.filter(id=info['product']).first()
            purchase = Purchase.objects.create(

                cart = cart,
                quantity = info['quantity'], 
                product= product,
            )
            
            return Response(request.data , status=HTTP_200_OK)

        else:
            return Response({"Error !" : "Invalid Input Format"} , status=HTTP_404_NOT_FOUND)



class PurchaseEditDeleteView(APIView):

    def get(self, request , purchase_id):

        purchase = Purchase.objects.filter(id=purchase_id)
        serializer = PurchaseSerializer(purchase , many=True)
        return Response(serializer.data , status=HTTP_200_OK)


    def put(self , request , purchase_id):

        info = request.data
        if info.keys() == {'quantity'}:

            purchase = Purchase.objects.filter(id=purchase_id)
            if purchase.update(quantity=info['quantity']):

                return Response({"Success" : "Quantity Updated" , "purchase item" : purchase_id} , status=HTTP_201_CREATED)
            
            else:

                return Response({"Error !" : "Error updating"} , status=HTTP_404_NOT_FOUND)
        
        else:

            return Response({"Error !" : "Invalid Input Format"} , status=HTTP_404_NOT_FOUND)


    def delete(self , request , purchase_id):

        purchase = Purchase.objects.filter(id=purchase_id)
        if purchase.delete():

            return Response({"Success" : "Quantity Deleted"} , status=HTTP_201_CREATED)
        
        else:
    
            return Response({"Error !" : "Error Deleting"} , status=HTTP_404_NOT_FOUND)



class CustomerAllOrdersView(APIView):

    def get(self , request , cart_id):

        orders = Order.objects.filter(cart=cart_id)
        serializer = OrderSerializer(orders , many=True)

        return Response(serializer.data , status=HTTP_200_OK)

    def post(self, request , cart_id):

        info = request.data
        if info.keys() == {'delivery' , 'status'}:

            cart = Cart.objects.filter(id=cart_id).first()
            delivery = DeliveryPerson.objects.filter(id=info['delivery']).first()
            order = Order.objects.create(

                delivery = delivery,
                status   = info['status'],
                cart     = cart,
            )
            if order:
                return Response(info , status=HTTP_201_CREATED)

            else:
                return Response({"Error !" : "Order Creation Failed"} , status=HTTP_404_NOT_FOUND)
        else:

            return Response({"Error !" : "Invalid Input Format"} , status=HTTP_404_NOT_FOUND)


class OrderEditDeleteView(APIView):

    def get(self,request , order_id):

        order = Order.objects.filter(id=order_id)
        serializer = OrderSerializer(order , many=True)

        return Response(serializer.data , status=HTTP_200_OK)

    def put(self, request , order_id):

        info = request.data
        if info.keys() == {'status'}:

            order = Order.objects.filter(id=order_id)
            order.update(status = info['status'])
            serializer = OrderSerializer(order , many=True)
            return Response(serializer.data , status=HTTP_201_CREATED)

        else:

            return Response({"Error !" : "Invalid Input Format"} , status=HTTP_404_NOT_FOUND)


    def delete(self , request , order_id):

        order = Order.objects.filter(id=order_id)
        if order.delete() :

            return Response({"Success" : "Deleted"} , status=HTTP_202_ACCEPTED)

        else:

            return Response({"Error" : "Not Deleted"} , status=HTTP_404_NOT_FOUND)