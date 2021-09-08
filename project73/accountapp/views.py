from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def registeruser(request):
    form=UserCreationForm()
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='accountapp/register.html'
    context={'form':form}
    return render(request,template_name,context)

def loginuser(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('addproduct')
        else:
            messages.error(request,'Invalid cridentials')
    template_name='accountapp/login.html'
    return render(request,template_name)

def logoutuser(request):
    logout(request)
    return redirect('register')

def changepassword(request):
    if request.method =='POST':
        u=request.POST.get("uname")
        p=request.POST.get("password")
        new=request.POST.get("new_password")
        con=request.POST.get("conform_password")

        user=authenticate(username=u,password=p)
        if user and new==con:
            user=User.objects.get(username=u)
            conform=str(con)
            user.set_password(conform)
            user.save()
            return redirect('login')
        else:
            messages.error(request,'plz enter correct content')
    template_name='accountapp/changepassword.html'
    return render(request,template_name)


