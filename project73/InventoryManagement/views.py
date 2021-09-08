from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
@login_required
def showproduct(request):
    prod=Product.objects.all()
    template_name='showproduct.html'
    context={'prod':prod}
    return render(request,template_name,context)
    
@login_required
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

@login_required
def deleteproduct(request,delete):
    prod=Product.objects.get(id=delete)
    prod.delete()
    return redirect('showproduct')
    


