from rest_framework.serializers import ModelSerializer
from . models import ProductGroup , Brand , Product

class ProductGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'



class BrandSerializer(ModelSerializer):


    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(ModelSerializer):

  
    
    class Meta:
        model = Product
        fields = '__all__'