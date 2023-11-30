from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

from .views import generate_image


urlpatterns = [
   
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('numberplates',views.numberplates,name='numberplates'),
    path('nameboards',views.nameboards,name='nameboards'),
    path('about',views.about,name='about'),
    path('desknameplates',views.desknameplates,name='desknameplates'),

    path('categories',views.categories,name='categories'),

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),

    path('product/<pid>/',views.product_detail_view,name='product_detail_view'),


    path('generate-image/', generate_image, name='generate_image'),
]


