from django.contrib import admin
from app.models import *

# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user','title','product_image','price','category','featured','product_status','pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['createdby','product', 'content', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'date']

admin.site.register(banner)
admin.site.register(collections)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Category_banner)

admin.site.register(Review,ReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
