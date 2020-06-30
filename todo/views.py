from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from todo.forms import CreateUserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# class MemeView(TemplateView):
#     template_name ='index.html'

@login_required(login_url='login')
def MemeView(request):
    return render(request, "index.html")

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserform()

        if request.method =='POST':
            form = CreateUserform(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,"Account was succesfuly created for "+ user)
                return redirect('login')
        context = {'form':form}
        return render(request, "register.html",context)


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username , password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
                
        context={}
        return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')
