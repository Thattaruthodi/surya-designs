from django.shortcuts import render,redirect
from django.contrib.auth.models import User  
from django.contrib import messages ,auth
from .models import Product
# Create your views here.
# def index(request):

   
#    products= Product.objects.filter(product_status="published",featured=True)

#    context = {
#               "products":products
#               }

#    return render(request,"index.html",context)

def index(request):
    query = request.GET.get('search-product', '')  

    if query:
      products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()
    context = {
        "products": products,
        "search_query": query,  
    }
    return render(request, "index.html", context)

def shop(request):
   products = Product.objects.all()
   context = {
        "products": products,
       
      }
   return render(request,"shop.html",context)

def nameboards(request):
    return render(request,"nameboards.html")

def numberplates(request):
    return render(request,"numberplates.html")

def about(request):
    return render(request,"about.html")


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
         messages.warning(request,'password is not matching') 
          
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


# dict_main_banner= {
   #    'main_banner':Main_banner.objects.all()
   # }
   # dict_banner= {
   #    'banners':Main.objects.all()
   # }
   # dict_product= {
   #    'products':Product.objects.filter(product_status="published",featured=True),
       
        
   # }
   # **dict_banner,
    #   **dict_main_banner,