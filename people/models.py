from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='user')
    phone_number = models.FloatField(blank=False)

    def __str__(self):
        return self.user.username

    
        

class CustomerAddress(models.Model):

    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    district = models.CharField(blank=False, max_length=150)
    town     = models.CharField(blank=False, max_length=150)
    locality = models.CharField(blank=False, max_length=150)
    street   = models.CharField(blank=False, max_length=150)
    house_number = models.CharField(blank=False, max_length=150)

    def __str__(self):
        return "Customer = : "+str(self.customer)+" District : "+self.district+" Town : "+self.house_number

class DeliveryPerson(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.FloatField(blank=False)
    vehicle_reg_number = models.CharField(blank=False , max_length=150)
    description = models.TextField()
    profile_photo = models.URLField(blank=False , max_length=255)


    def __str__(self):
        return self.user.username