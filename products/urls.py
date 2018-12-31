from django.urls import path
from .views import *
app_name = 'products'

urlpatterns = [

    path('groups/all/' , ViewProductGroup.as_view() , name='all-groups'),
    path('group/detail/<pk>' , DetailProductGroup.as_view() , name='group-details'),

    path('brands/all/' , ViewBrands.as_view() , name='all-brands'),
    path('brand/detail/<pk>' , DetailBrand.as_view() , name='brand-details'),

    path('all/' ,ViewProducts.as_view() , name ='all-products' ),
    path('detail/<pk>' , DetailProduct.as_view() , name='product-details'),


]
