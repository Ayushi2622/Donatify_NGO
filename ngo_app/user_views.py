from django.shortcuts import render,redirect
from .models import User,FeedBack,Donation
from django.contrib import messages

import qrcode
import base64
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only for testing, in production use proper CSRF token headers with fetch
def generate_qr(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if not amount:
            return JsonResponse({'error': 'Amount is required'}, status=400)

        # You can use your UPI format or just amount text
        qr_data = f"upi://pay?pa=ayushipandey26feb@okicici&am={amount}&cu=INR"

        img = qrcode.make(qr_data)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return JsonResponse({'image': img_str})


def user_logout(request):
   request.session.flush()
   messages.success(request,"Successfully logged out!!")
   return redirect("login")

def user_home(request):
   ##fetching email from session to identify the user.
   if request.method=="GET":
     user_email=request.session["web_key"]
     User_Obj=User.objects.get(email=user_email)    # since it will return a single object therefore using GET.
     ## sending data from view to html (template) page.
     ## creating a dictionary and bind data with a key.
     ## send that dict with render function.
     user_dict={
        "user_key": User_Obj

     }
     return render(request,"ngo_app/user/user_home.html",user_dict)
   


def user_login(request):
    if request.method=="GET":
       return render(request,"ngo_app/user/user_login.html")
    if request.method=="POST":
       user_email=request.POST["email"]
       user_password=request.POST["password"]
       ## select * from user where email=user_email and password=user_password.
       user_list=User.objects.filter(email=user_email, password=user_password)
       ## filter method is used to filter the data on the specified contents.
       if len(user_list)>0:
          request.session["web_key"]=user_email  #binding email in a session to track user for multiple requests.
          ## web key is used to identify a user uniquely, it is equivalent to roll no.
          return redirect("user_home")
       else:
          messages.error(request,"Invalid Credentials,Try Again!!")
          return redirect("login")
       

       

def user_feedback(request):
    if request.method=="GET":
      return render(request,'ngo_app/user/user_feedback.html')
    if request.method=="POST":
       user_name=request.POST["name"]
       user_email=request.session["web_key"]
       user_rating=request.POST["rating"]
       user_remarks=request.POST["remarks"]

       feedback_obj=FeedBack(name=user_name,email=user_email,rating=user_rating,remarks=user_remarks)
       feedback_obj.save()
       messages.success(request,"🙏Thank You For Your Time🙏")
       return redirect("feedback")


def user_registration(request):
    if request.method=="GET":
      return render(request,'ngo_app/user/user_registration.html')
    if request.method=="POST":
       user_email= request.POST["email"]           #control name input field
       user_password=request.POST["password"]
       user_name=request.POST["name"]
       user_phone=request.POST["phone"]
       user_pic=request.FILES["profile_pic"]
       ## ORMapping frameworks ##
       ## create object of user model 
       ## set values
       ## save object -> it automatically stores values in table

       user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
       user_obj.save()
       return redirect("login")
    
def add_donation(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/add_donation.html')
    if request.method=="POST":
       email = request.session["web_key"]
       amount = request.POST["amount"]
       aadhaar = request.FILES["aadhar"]
       transaction_id = request.POST["transaction_id"]
       user=User.objects.get(email=email)
       donation = Donation(user=user,amount=amount,aadhaar=aadhaar,transaction_id=transaction_id)
       donation.save()
       messages.success(request,"Thank You For Donation!!🙏🙏")
       return redirect("add_donation")
    
def donation_history(request):
     if  request.method=="GET":
      u_email = request.session["web_key"]

      user_obj=User.objects.get(email=u_email)
     donation_list=Donation.objects.filter(user=user_obj)
     donation_dict={
        "donation_key":donation_list
     }
     return render(request,'ngo_app/user/donation_history.html',donation_dict)

def edit_profile(request):
   if request.method=="GET":
       user_email=request.session["web_key"]
       User_Obj=User.objects.get(email=user_email) 
       user_dict={
        "user_key": User_Obj
      }
       return render(request,"ngo_app/user/edit_profile.html",user_dict)
   if request.method=="POST":
      user_name=request.POST["name"]
      user_phone=request.POST["phone"]
      user_pic=request.FILES.get("pic")
      user_email=request.session["web_key"]
      User_Obj=User.objects.get(email=user_email) 
      if user_pic is not None:
         User_Obj.profile_pic=user_pic
      User_Obj.name=user_name
      User_Obj.phone=user_phone
      User_Obj.save()
      messages.success(request,"Profile Updated Successfully👍👍")
      return redirect("user_home")
      

   
    


  
    