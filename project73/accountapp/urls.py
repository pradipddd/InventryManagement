from django.urls import path
from .views import changepassword, registeruser,loginuser,logoutuser

urlpatterns=[
    path('register/',registeruser,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('change/',changepassword,name='change')
]