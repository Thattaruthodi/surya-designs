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

class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    class Meta:
        verbose_name="contact"
        verbose_name_plural="contact"



    def __str__(self):
        return self.full_name