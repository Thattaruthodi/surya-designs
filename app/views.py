from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User  
from django.contrib import messages ,auth
from .models import *
from django.db.models import Count,Avg
# from app.forms import Reviewform

# Create your views here.
def index(request):
    dict_banner= {
      'banner':banner.objects.all()
     }
    dict_collections= {
      'collections':collections.objects.all()
     }
    dict_product= {
      # 'products':Product.objects.all().order_by("-id")
        'products':Product.objects.filter(product_status="published",featured="True")
       
        
   }
    context = {
      **dict_banner,**dict_product,**dict_collections
   }
    return render(request, "core/index.html",context)


def category_list_view(request):
     categories = Category.objects.all().annotate()
   
     context = {
          "categories":categories
     }
     return render(request, "core/category_list.html",context)

def product_list_view(request):
     products = Product.objects.filter(product_status="published")
     context = {
          "products":products
     }
     return render(request, "core/product_list.html",context)

def category_product_list_view(request,cid):
     category = Category.objects.get(cid=cid)
     products = Product.objects.filter(product_status="published",category=category)
           
     context = {
          "category":category,
          "products":products
      }
     return render(request, "core/category-product-list.html",context)

def product_detail_view(request,pid):
     product = Product.objects.get(pid=pid)
     p_image = product.p_images.all()
     products = Product.objects.filter(category=product.category).exclude(pid=pid)


     context = {
          'p':product,
          'p_image':p_image,
          'products':products,

     }
     return render(request, "core/product-detail.html",context)