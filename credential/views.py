from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['txt_uname']
        firstname=request.POST['txt_fname']
        lastname = request.POST['txt_lname']
        email=request.POST['email']
        password=request.POST['pass']
        con_pass=request.POST['con_pass']
        if password==con_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                messages.info(request,"user created")
                return redirect("login")
        else:
            print("Passwords do not match")
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('demo')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('demo')