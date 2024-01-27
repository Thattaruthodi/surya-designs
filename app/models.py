from django.db import models
from django.contrib.auth.models import User
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.utils import timezone
from django.conf import settings

# Create your models here.

STATUS_CHOICES = (
    ("process","processing"),
    ("shipped","shipped"),
    ("delivered","delivered"),
)
STATUS = (
    ("draft","Draft"),
    ("disabled","disabled"),
    ("rejected","rejected"),
    ("in review","in review"),
    ("published","published"),

)
RATING = (
    (None, 'No Rating'),
    ("1", "★☆☆☆☆"),
    ("2", "★★☆☆☆"),
    ("3", "★★★☆☆"),
    ("4", "★★★★☆"),
    ("5", "★★★★★"),
)



class banner(models.Model):
    
    heading = models.CharField(max_length=100)
    banner_image1 = models.ImageField(upload_to='banners')
    banner_image2 = models.ImageField(upload_to='banners')

    class Meta:
        verbose_name_plural = "banners"

    def __str__(self):
        return self.heading

class collections(models.Model):
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners')

    class Meta:
        verbose_name_plural = "collections"

    def __str__(self):
        return self.type

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20,prefix = "cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="designs")
    image = models.ImageField(upload_to="category" , default="category.jpg")
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50 height="50" />' % (self.image.url))
     
    def __str__(self):
        return self.title
    
class Category_banner(models.Model): 
    heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banners")

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20,prefix = "cat",alphabet="abcdefgh12345")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="category")

    
    title = models.CharField(max_length=100,default="fresh")
    image = models.ImageField(upload_to="user_directory_path",default="product.jpg")
    image_hover = models.ImageField(upload_to="user_directory_path",default="product.jpg")
    description = models.TextField(null=True,blank=True,default="this is the product")

    price = models.DecimalField(max_digits=99999999999999,decimal_places=2 ,default="1.99")
    old_price = models.DecimalField(max_digits=99999999999999,decimal_places=2 ,default="2.99")
    specifications = models.TextField(null=True,blank=True)
    # tags = models.ForeignKey(tags,on_delete=models.SET_NULL,null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")   

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    digital = models.BooleanField(default=True)
    
    sku = ShortUUIDField(length=4, max_length=10, prefix="sku", alphabet="12453789664")
    date = models.DateTimeField(null=True,blank=True)
     
    class Meta:
        verbose_name_plural = "products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50 height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
        
    # def get_percentage(self):
    #     new_price = (self.price / self.old_price)*100
    #     return new_price
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images" , default="product.jpg")
    product = models.ForeignKey(Product,related_name="p_images", on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product Images"


# class ProductReview(models.Model):
#     user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   

#     product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
#     date = models.DateTimeField(auto_now_add=True)
#     review = models.TextField()
#     rating = models.IntegerField(choices=RATING, default=2)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Product Reviews"

#     def __str__(self):
#         return self.product.title
    
#     def get_rating(self):
#         return self.rating

class Review(models.Model):
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    createdby = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "wishlist"

    def __str__(self):
        return self.product.title