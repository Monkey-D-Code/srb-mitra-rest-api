from django.contrib import admin
from . models import ProductGroup , Product , Brand
# Register your models here.

admin.site.register(ProductGroup)
admin.site.register(Brand)
admin.site.register(Product)