
from django.urls import path
from . import views
urlpatterns = [
    
    path("sign_up",views.signup,name='sign_up'),
    path("home/",views.home,name='home'),
    path("profile/",views.profile,name='profile_page'),
    path("login/",views.log_in,name='log_in_page'),
    path("logout/",views.log_out,name='log_out_page'),
    path("pass_change/",views.pass_change,name='pass_change'),
    path("pass_change_2/",views.pass_change_2,name='pass_change_2'),

]