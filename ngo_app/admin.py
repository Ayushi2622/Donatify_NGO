from django.contrib import admin
from .models import Contact,FeedBack,User,Campaign,Donation
class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","query","date"]
class FeedBack_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remarks","date"]
class User_Admin(admin.ModelAdmin):
    list_display=["name","email","password","phone","date"]
class Campaign_Admin(admin.ModelAdmin):
    list_display=["title","description","from_date","to_date","venue"]
class Donation_Admin(admin.ModelAdmin):
    list_display=["user","amount","aadhaar","transaction_id","date","paymentstatus"]


admin.site.register(Contact,Contact_Admin)
admin.site.register(FeedBack,FeedBack_Admin)
admin.site.register(User,User_Admin)
admin.site.register(Campaign,Campaign_Admin)
admin.site.register(Donation,Donation_Admin)

admin.site.site_header="NGO Admin DashBoard"
admin.site.site_title="Be the Reason Someone Smiles Today"
admin.site.index_title="Donatify NGO"
