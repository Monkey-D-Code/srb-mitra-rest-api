from django.db import models

# Create your models here.
class ProductGroup(models.Model):

    name = models.CharField(blank=False , max_length=150)
    desc = models.TextField()
    photo = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(blank=False, max_length=255)
    group = models.ForeignKey(ProductGroup , on_delete=models.CASCADE , null=True ,blank=False)

    desc = models.TextField()
    logo = models.URLField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):

    rating_options = (
        ('N' , 'No Rating'),
        ('VB' , 'Very Bad'),
        ('B' , 'Bad'),
        ('A' , 'Average'),
        ('G' , 'Good'),
        ('VG' , 'Very Good'),
        ('E' , 'Excellent'),
    )
    name = models.CharField(blank=False , max_length=255)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE , null=True ,blank=False)
    sold_unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.URLField(max_length=255)
    rating  = models.CharField(choices=rating_options , max_length=50 , default='N')

    def __str__(self):
        return self.name