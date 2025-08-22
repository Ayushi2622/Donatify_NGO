from django.urls import path,include
from .import views,user_views
urlpatterns = [
    path("",views.home,name="home"),
    path("contact/",views.contact_us,name="contact"),
    path("about/",views.about_us,name="about"),
    path("view_campaigns/",views.view_campaigns,name="view_campaigns"),
    path("user_feedback/",user_views.user_feedback,name="feedback"),
    path("user_login/",user_views.user_login,name="login"),
    path("user_registration/",user_views.user_registration,name="registration"),
    path("education/",views.education,name="education"),
    path("health/",views.health,name="health"),
    path("safety/",views.safety,name="safety"),
    path("participation/",views.participation,name="participation"),
    path("user_home/",user_views.user_home,name="user_home"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    path("add_donation/",user_views.add_donation,name="add_donation"),
    path('generate_qr/', user_views.generate_qr, name='generate_qr'),
    path("donation_history/",user_views.donation_history,name="donation_history"),
    path("edit_profile/",user_views.edit_profile,name="edit_profile"),


   
]
