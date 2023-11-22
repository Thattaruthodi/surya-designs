from django.shortcuts import render,redirect
from django.contrib.auth.models import User  
from django.contrib import messages ,auth
from .models import *

from django.http import JsonResponse
# Create your views here.
def index(request):

   dict_main_banner= {
      'main_banner':Main_banner.objects.all()
   }
   dict_banner= {
      'banners':Main.objects.all()
   }
   
   context = {**dict_banner,**dict_main_banner}
   return render(request,"index.html",context)

def shop(request,val):
 
    return render(request,"shop.html")

def nameboards(request):
    return render(request,"nameboards.html")

def numberplates(request):
  
   return render(request,"numberplates.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def ajax_contact(request):
    pass




def form(request):
    
    return render(request,"form.html")

def ajax_form_demo(request):
    full_name =request.GET['full_name']
    email =request.GET['email']
    phone=request.GET['phone']
    subject=request.GET['subject']
    message =request.GET['message']

    form =Contact.objects.create(
       full_name=full_name,
       email=email,
       phone=phone,
       subject=subject,
       message=message,

    )
    data ={
       "bool":True,
       "message":"message sent successfully"
    }
    return JsonResponse({"data":data})



def product_detail(request):
    return render(request,"product_detail.html")

def register(request): 
   if request.method == 'POST' : 
      first_name=request.POST['first_name'] 
      last_name=request.POST['last_name'] 
      username=request.POST['username'] 
      email=request.POST['email'] 
      password1=request.POST['password1'] 
      password2=request.POST['password2'] 
       
      
 
 
      if password1 == password2 : 
         if User.objects.filter(username=username).exists(): 
             messages.info(request,'username is taken') 
             return redirect('register') 
         elif User.objects.filter(email=email).exists()  : 
            messages.info(request,'email is taken') 
            return redirect('register') 
         else:      
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name) 
            user.save(); 
            
            messages.success(request,"congratulation User Registered Successfully") 
      else: 
         messages.warning(request,'password is not matching  ') 
          
         return redirect('register') 
      return redirect('/')  
   else: 
      return render(request,'register.html')   
    
 
def  login(request): 
   if request.method == 'POST': 
      username=request.POST.get('username') 
      password=request.POST.get('password') 
       
     
 
      user =auth.authenticate(username=username,password=password) 
       
      if user is not None: 
         auth.login(request,user) 
         return redirect('/')  
      else: 
         messages.info(request,'invalid credentials') 
         return redirect('login') 
   else: 
      return render(request,'login.html') 
      
def logout(request): 
   auth.logout(request) 
   return redirect('login')  
