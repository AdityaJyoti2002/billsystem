from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import GeneratePdf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from .models import  signups
# Create your views here.

@login_required(login_url='login')

def index(request):
    return render(request, "index.html")

# def save(request):

#     return render(request, "index.html")

def generatepdf(request):
    if request.method == "POST":
      
        Samsung_TV = request.POST.get("Samsung_TV")
        phone2 = request.POST.get("JBL_Speaker")
        phone3 = request.POST.get("Macbook_Ai")
        phone4 = request.POST.get("Iphone_11_PRO")
        dt = request.POST.get("date")
        name = request.POST.get("name1")
        number = request.POST.get("number1")
        payment = request.POST.get("paymentoption")
        SamsungTV = 30000
        JBLSpeaker = 500000
        MacbookAi = 10000
        Iphone11PRO = 10000
        total = (int(Samsung_TV )*SamsungTV + int(phone2)*JBLSpeaker + int(phone3)*MacbookAi + int(phone4)*Iphone11PRO)
        save = GeneratePdf(field1=Samsung_TV, field2=phone2, field3=phone3, field4=phone4, field5=dt, field6=name, field7=number)
        save.save()
        return render(request, "pdf.html",{"Samsung_TV": Samsung_TV, "JBL_Speaker": phone2, "Macbook_Ai": phone3, "Iphone_11_PRO": phone4, "date": dt, "total": total, "name1": name, "number1": number, "paymentoption": payment})

    return render(request, "index.html")

def SignUp(request):
    if request.method =="POST":

        Email = request.POST.get("email")
        username = request.POST.get("name")
        password = request.POST.get("Password")
        cfmpassword =request.POST.get("cmf")

        if password!=cfmpassword:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            myuser= User.objects.create_user(Email, username, password)
            myuser.save()
     
        return redirect("login")

    return render(request, "SignUp.html")

def loginup(request):
    if request.method =="POST":

        # Email = request.POST.get("email")
        username1 = request.POST.get("name")
        password1 = request.POST.get("Password")
        # cfmpassword =request.POST.get("cmf")
        user=authenticate(request,username=username1,password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')

            # return HttpResponse ("Username or Password is incorrect!!!")
        else:
            # login(request,user)
            # return redirect('home')
            return HttpResponse ("Username or Password is incorrect!!!")


    return render(request, "login.html")

def logoutpage(request):
    logout(request)
    return redirect("login")