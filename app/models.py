from django.db import models
from django.contrib.auth.models import User
# from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.utils import timezone

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
    ("1","★☆☆☆☆"),
    ("2","★★☆☆☆"),
    ("3","★★★☆☆"),
    ("4","★★★★☆"),
    ("5","★★★★★"),

    
)

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

# Create your models here.
class Main_banner(models.Model):
    sub_head = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    main_banner_image = models.ImageField(upload_to='banners')
    
class Main(models.Model):
    head=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    image_banner = models.ImageField(upload_to='banners',null=True)




    


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20,prefix = "cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="designs")
    image = models.ImageField(upload_to="category" , default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50 height="50" />' % (self.image.url))
     
    def __str__(self):
        return self.title
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20,prefix = "cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default="nest")
    image = models.ImageField(upload_to="user_directory_path",default="vendor.jpg")
    description = models.TextField(null=True,blank=True,default="amazing vendor")

    address = models.CharField(max_length=100,default="123 main street")
    contact = models.CharField(max_length=100,default="452236365")
    chat_resp_time = models.CharField(max_length=100,default="100")
    shipping_on_time = models.CharField(max_length=100,default="100")
    authentic_rating = models.CharField(max_length=100,default="100")
    days_return = models.CharField(max_length=100,default="100")
    warranty_period = models.CharField(max_length=100,default="100")

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50 height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20,prefix = "cat",alphabet="abcdefgh12345")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    
    title = models.CharField(max_length=100,default="fresh")
    price = models.DecimalField(max_digits=99999999999999,decimal_places=2 ,default="1.99")
    old_price = models.DecimalField(max_digits=99999999999999,decimal_places=2 ,default="2.99")
    image = models.ImageField(upload_to="user_directory_path",default="product.jpg")
    size = models.TextField(null=True,blank=True)
    style = models.TextField(null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    designation = models.TextField(null=True,blank=True)

    
    description = models.TextField(null=True,blank=True,default="this is the product")


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
        
    def get_percentage(self):
        new_price = (self.price / self.old_price)*100
        return new_price
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images" , default="product.jpg")
    product = models.ForeignKey(Product,related_name="p_images", on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product Images"
    
class ProductReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

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
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title
    
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "address"

