from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


app_name = "core"

urlpatterns = [
   
    path('',views.index,name='index'),
    path('products/',views.product_list_view,name='product-list'),
    path('product/<pid>/',views.product_detail_view,name='product_detail'),
  
    path('category/', views.category_list_view, name='categories'),
    path('category/<cid>/', views.category_product_list_view, name='category_product_list'),

    # path('search',views.search,name='search'),


    # path('numberplates',views.numberplates,name='numberplates'),
    # path('nameboards',views.nameboards,name='nameboards'),
    # path('gst_nameplates',views.gst_nameplates,name='gst_nameplates'),
    # path('number_signs',views.number_signs,name='number_signs'),

    # path('about',views.about,name='about'),

    # path('category',views.category,name='category'),

    # path('register',views.register,name='register'),
    # path('login',views.login,name='login'),

   


]


