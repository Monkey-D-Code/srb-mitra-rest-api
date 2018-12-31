from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework import permissions


from django.shortcuts import get_object_or_404

from . models import *
from . serializers import *
# Create your views here.

# PRODUCT GROUP CONNECTED VIEWS

class ViewProductGroup(ListCreateAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer


class DetailProductGroup(RetrieveDestroyAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer



# VIEWS CONNECTED TO BRAND

class ViewBrands(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class DetailBrand(RetrieveDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# VIEWS CONNECTED TO PRODUCTS

class ViewProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
