from django.db import models

# Create your models here.
class Main_banner(models.Model):
    sub_head = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    main_banner_image = models.ImageField(upload_to='banners')
    
class Main(models.Model):
    head=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    image_banner = models.ImageField(upload_to='banners',null=True)


class Product(models.Model):

    title = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='products')
    
    def __str__(self) :
        return self.title