from django.shortcuts import render,redirect
from .models import Contact,Campaign,FeedBack,User
from django.contrib import messages

# Create your views here.

def view_campaigns(request):
   camp_list=Campaign.objects.all()    #select * from service.
   context={
      "camp_key":camp_list
   }
   return render(request,'ngo_app/html/view_campaigns.html',context)
  

def home(request):
    feedback=FeedBack.objects.all()
    data=[]
    for f in feedback:
       data.append(
          {
             "rating":f.rating,
             "remarks":f.remarks,
             "name":f.name,
             "profile_pic":User.objects.get(email=f.email).profile_pic
          }
       )
    feedback_dict={
       "feedback_key":data
    
    }
       
    return render(request,'ngo_app/html/index.html',feedback_dict)

def contact_us(request):
  if request.method=="GET":
    return render(request,'ngo_app/html/contact_us.html')
  if request.method=="POST":
    user_name=request.POST["name"]
    user_email=request.POST["email"]
    user_phone=request.POST["phone"]
    user_query=request.POST["query"]
       
    ##fetch value from all text fields.
    # create object of contact model and save

    contact_obj=Contact(name=user_name,email=user_email,phone=user_phone,query=user_query)
    contact_obj.save()
    messages.success(request,"🙏Thank You, We'll reach to you soon!!🙏")
    return redirect("contact")

def about_us(request):
    return render(request,'ngo_app/html/about_us.html')

def education(request):
    return render(request,'ngo_app/html/education.html')

def health(request):
    return render(request,'ngo_app/html/health & nutrition.html')

def safety(request):
    return render(request,'ngo_app/html/safety & protection.html')

def participation(request):
    return render(request,'ngo_app/html/Child Participation.html')


