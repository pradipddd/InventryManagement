from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','date','provider','name_of_product','price','quantity','amount','stock']
admin.site.register(Product,ProductAdmin)
