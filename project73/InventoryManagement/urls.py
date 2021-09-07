from django.urls import path
from .views import addproduct, showproduct, updateproduct,deleteproduct

urlpatterns=[
    path('add/',addproduct,name='addproduct'),
    path('show/',showproduct,name='showproduct'),
    path('update/<int:update>',updateproduct,name='update'),
    path('delete/<int:delete>',deleteproduct,name='delete'),
    
    

    
    
]