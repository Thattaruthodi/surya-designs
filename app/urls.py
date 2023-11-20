from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('numberplates',views.numberplates,name='numberplates'),
    path('nameboards',views.nameboards,name='nameboards'),
    path('about',views.about,name='about'),

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),

    path('product_detail',views.product_detail,name='product_detail'),


]
