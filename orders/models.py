from django.db import models
from people.models import *
from products.models import *
# Create your models here.


class Cart(models.Model):
    
    status_choices = (
        ('O' , 'Ordered'),
        ('S' , 'Saved'),
        ('D' , 'Delivered'),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    status = models.CharField(status_choices, max_length=50 , default='S')

    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return "Customer : "+str(self.customer)+" Status : "+self.status


class Purchase(models.Model):

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    
    quantity = models.DecimalField(blank=False , max_digits=8, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return "Product : "+str(self.product)

class Order(models.Model):

    status_choices = (
        ('R' , 'Recived'),
        ('O' , 'On The Way'),
        ('D' , 'Delivered'),
    )

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    delivery = models.ForeignKey(DeliveryPerson, on_delete=models.PROTECT)
    

    status = models.CharField(status_choices, max_length=50)


    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return " Status : "+self.status


