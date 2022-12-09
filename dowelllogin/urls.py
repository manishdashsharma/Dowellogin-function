from django.urls import path
from dowelllogin.views import home ,page

pp_name = "dowelllogin" 
urlpatterns =[
    path('',home, name= 'home'),
    path('page/',page, name= 'home'),
]