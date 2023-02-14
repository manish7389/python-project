import re
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm
from services.models import services
from news.models import News
from django.core.paginator import Paginator
from contactinqury.models import contactinqury

def hoempage(request):
    servicesdata = services.objects.all().order_by('-services_title')[:6]
    newsdata = News.objects.all()
    # for a in servicesdata:
    #     print(a.services_icon)
    # print(services)
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            servicesdata = services.objects.filter(services_title__icontains=st)
    paginator = Paginator(servicesdata,2)
    page_number =  request.GET.get('page')
    servicesdatafinal = paginator.get_page(page_number)
    total_page = servicesdatafinal.paginator.num_pages

    data = {
        'servicesdata':servicesdatafinal,
        'lastpage': total_page,
        'totalpagelist':[n+1 for n in range(total_page)],
        'newsdata':newsdata,
        'title' : 'Home page',
        'bdata' : 'Welcome To My Home Page new',
        'clist' : ['python','java','django','javascript'],
        'numbers' : [10,20,30,40,50,60,70],
        'student_detail': [
            {'name':'manish','phone':'9984743980'},
            {'name' : 'herry','phone':'9836748937'},
        ]
    }
    return render(request, "index.html", data)


def newsdetails(request,slug):
    newsdetails=News.objects.get(news_slug=slug)
    data={
       "newsdetails":newsdetails,
    }
    return render(request,"newsdetails.html", data)


def aboutus(request):
    return HttpResponse("welcom to my project page about us")

def coures(request):
    return HttpResponse("welcome to my project corse page")

def couresdetails(request, couresid):
    return HttpResponse(couresid)

def userform(request):
    finalans=0
    # fn = userform()
    try:
        if request.method=="GET":
            output=request.GET.get("output")
            return render(request,"userform.html",{'gettingvalue':output})
            # n1 = int(request.GET["num1"])
            # n2 = int(request.GET["num2"])                  
            n1 = int(request.GET.get("num1"))
            n2 = int(request.GET.get("num2"))
            finalans=n1+n2
    except:
        pass
    return render(request,"userform.html",{'output':finalans})

def userform2(request):
    finalans=0
    fn = userForm()

    data={'form':fn}
    try:
        if request.method=="POST":
        # n1 = int(request.GET["num1"])
        # n2 = int(request.GET["num2"])                  
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            finalans=n1+n2
            data={'form':fn,
                "n1":n1,
                "n2":n2,
                "output":finalans,
            }
            url= "/userform?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform2.html",data)

def calculator(request):
    c =""
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get("num1"))
            n2 = eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            if opr=="+":
                c = n1+n2
            elif opr=="-":
                c = n1-n2
            elif opr=="*":
                c = n1*n2
            elif opr=="/":
                c = n1/n2
    except:
        c = "Invalid input please select right value for calculate"
    return render(request,"calculator.html", {"c":c})



def contactInqury(request):

    return render(request,"contactinqury.html")

def saveinqury(request):
    n=''
    if request.method == "POST":
        fname = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        massage = request.POST.get('massage')

        en = contactinqury(name=fname,last_name=last_name,email=email,phone=phone,massage=massage)

        en.save()
        n='DATA INSERTED SECESSESFULLY'

    return render(request,"contactinqury.html",{'n':n})
