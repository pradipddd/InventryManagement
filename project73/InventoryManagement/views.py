from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm


# Create your views here.

def addproduct(request):
    form=ProductForm()
    if request.method =='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='addproduct.html'
    context={'form':form}
    return render(request,template_name,context)

def showproduct(request):
    prod=Product.objects.all()
    template_name='showproduct.html'
    context={'prod':prod}
    return render(request,template_name,context)

def updateproduct(request,update):
    prod=Product.objects.get(id=update)
    form=ProductForm(instance=prod)
    if request.method =='POST':
        form=ProductForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='addproduct.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteproduct(request,delete):
    prod=Product.objects.get(id=delete)
    prod.delete()
    return redirect('showproduct')
    


