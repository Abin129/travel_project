from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        un=request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        em = request.POST['email']
        ps = request.POST['password']
        cps = request.POST['c_pass']

        if ps==cps:
            if User.objects.filter(username=un).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif  User.objects.filter(email=em).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=un,password=ps,email=em,first_name=fn,last_name=ln)
                user.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request, "page not found")
            return redirect('register')
        return redirect(('/'))
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        un=request.POST['username']
        ps= request.POST['password']
        user=auth.authenticate(username=un,password=ps)
        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
