from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User  
from django.contrib import messages ,auth
from .models import *
# Create your views here.



def index(request):

   dict_products= {
      'products':Product.objects.all()
   }
   
   dict_main_banner= {
      'main_banner':Main_banner.objects.all()
   }
   dict_banner= {
      'banners':Main.objects.all()
   }

   context = {
              **dict_products, **dict_main_banner,**dict_banner
              }

   return render(request,"index.html",context)

# def index(request):
#     query = request.GET.get('search-product', '')  

#     if query:
#       products = Product.objects.filter(title__icontains=query)
#     else:
#         products = Product.objects.all()
#     context = {
#         "products": products,
#         "search_query": query,  
#     }
#     return render(request, "index.html", context)

def categories(request):
   categories = Category.objects.all()

   context = {
    
        "categories":categories,
       
      }
   return render(request,"categories.html",context)

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

def desknameplates(request):
    return render(request,"desknameplates.html")



def product_detail_view(request,pid):
   #  product = Product.objects.get(pid=pid) 
   product = get_object_or_404(Product,pid=pid)
   p_image = product.p_images.all()

   context = {
       "p":product,
       "p_image":p_image
        }
   
   return render(request,"product_detail.html",context)



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



from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render

def generate_image(request):
    # Get the text you want to add dynamically
    dynamic_text = "Your dynamic text here"

    # Open an image using Pillow
    base_image = Image.open('static/images/illam-1.jpg')

    # Create a drawing context to add text to the image
    draw = ImageDraw.Draw(base_image)
    
    # Define font style and size
    font = ImageFont.truetype("", 36)

    # Calculate text size and position
    text_width, text_height = draw.textsize(dynamic_text, font=font)
    image_width, image_height = base_image.size
    text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)

    # Add the text to the image
    draw.text(text_position, dynamic_text, font=font, fill="white")

    # Save the modified image
    response = HttpResponse(content_type="image/jpeg")
    base_image.save(response, "JPEG")
    return response


