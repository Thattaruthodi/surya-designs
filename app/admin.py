
from django.contrib import admin
from app.models import Main_banner,Main,Product,Category,Vendor,ProductImages,ProductReview,Wishlist,Address
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user','title','product_image','price','featured','product_status','pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address', 'status']

admin.site.register(Main_banner)
admin.site.register(Main)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)


