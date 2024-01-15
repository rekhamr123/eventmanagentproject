from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username Exists")
               return redirect("http://127.0.0.1:8000/register/")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return redirect("http://127.0.0.1:8000/register/")
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,"Registration success")
                return redirect('/')
        else:
            messages.info(request,"Confirm password Not matched")
            return redirect("http://127.0.0.1:8000/register/")
    return render(request, 'reg.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Not registered")
            return redirect("http://127.0.0.1:8000/register/")
    return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
