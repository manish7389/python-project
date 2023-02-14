from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,HttpRequest
from register.models import register
from .form import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django .contrib.auth import authenticate, login,logout


def saveregister(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
          fm.save()
          messages.success(request,'Account Created Successfully !!')
    else:
        fm = RegisterForm()
        
    return render(request,"register.html", {'form':fm})

# Create your views here.

def login(request):
    if request.method == "POST":
        # fm = AuthenticationForm(request=request, data=request.POST)
        # fm = AuthenticationForm(request=request,data=request.POST)
        # if fm.is_valid():
            # uname = fm.cleaned_data['username']
            # upass = fm.cleaned_data['password']
            uname = request.POST['username']
            upass = request.POST['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request)
                # return HttpResponseRedirect('profile/')  
                return HttpResponseRedirect("register.html")      
    else:
        fm =AuthenticationForm()
        return render(request,"login.html",{'form':fm})


def profile(request):

    return render(request,'profile.html')

# def login(request):
#     logindata = register.objects.all()
#     try:
#         if request.method=="POST":
#             email= request.POST.get('email')
#             password= request.POST.get('password')
#             if email !=None and password !=None:
#                 logindata = register.object.filter(email=email)
#                 data={
#                     'logindata':logindata
#                 }

#         return render(request,"login.html",data)
#     except:
#         print("yha kuch to gadbadh he dyaaaa")
#         return render(request,"login.html")



# def saveregister(request):
#     n=''
#     try:
#         if request.method=="POST":
#             first_name=request.POST.get('first_name')
#             last_name=request.POST.get('last_name')
#             email=request.POST.get('email')
#             password=request.POST.get('password')
#             if first_name =='' or last_name =='' or email =='' or password =='':
#                 n='your information is incorrect please check and TRY AGAIN'
#                 return render(request,"register.html",{'n':n})
#             en=register( first_name= first_name,last_name=last_name,email=email,password=password)
#             en.save()
#             n='Registration successful : you can Login'
        
#         return render(request,"register.html",{'n':n})
#     except:
#         pass