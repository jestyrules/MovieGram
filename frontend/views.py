from django.shortcuts import render, redirect

from backend.models import productdb, categorydb
from frontend.models import Registerdb, Cartdb, Checkoutdb


# Create your views here.
def homepage(request):
    data = productdb.objects.all()
    cat = categorydb.objects.all()
    return render(request, "homepage.html", {'data': data, 'cat': cat})


def singlemov(request, proid):
    mov = productdb.objects.get(id=proid)
    cat = categorydb.objects.all()
    return render(request, "Singlemov.html", {'mov': mov, 'cat': cat})


def registermov(request):
    cat = categorydb.objects.all()
    return render(request, "Registermov.html", {'cat': cat})


def loginmov(request):
    cat = categorydb.objects.all()
    return render(request, "Loginmov.html", {'cat': cat})


def registersave(req):
    if req.method == "POST":
        un = req.POST.get('username')
        en = req.POST.get('email')
        ps = req.POST.get('password')
        obj = Registerdb(Username=un, Email=en, Password=ps)
        obj.save()
        return redirect(loginmov)


def userlogin(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if Registerdb.objects.filter(Username=user, Password=pwd).exists():
            request.session['username'] = user
            request.session['password'] = pwd
            return redirect(homepage)
        else:
            return redirect(loginmov)
    else:
        return redirect(loginmov)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)


def cartsave(request):
    if request.method == "POST":
        na = request.POST.get('moviename')
        la = request.POST.get('language')
        pr = request.POST.get('price')
        ca = request.POST.get('category')
        obj = Cartdb(MovieName=na, Language=la, Price=pr, Category=ca)
        obj.save()
        return redirect(homepage)


def cartdisplay(request):
    cat = categorydb.objects.all()
    data = Cartdb.objects.all()
    total_price = 0
    for i in data:
        total_price = total_price + i.Price
    return render(request, "cartdisplay.html", {'data': data, 'total': total_price, 'cat': cat})


def cartdelete(request, dataid):
    data = Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartdisplay)


def pro(request, catname):
    data = categorydb.objects.all()
    cat = productdb.objects.filter(CategoryName=catname)
    return render(request, "pro.html", {'data': data, 'cat': cat})


def checkout(request):
    return render(request, "checkout.html")


def checkoutsave(request):
    if request.method == "POST":
        us = request.POST.get('username')
        em = request.POST.get('email')
        cn = request.POST.get('contact')
        pl = request.POST.get('place')
        obj = Checkoutdb(Username=us, Email=em, Contact=cn, Place=pl)
        obj.save()
        return redirect(homepage)
