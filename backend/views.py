from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from backend.models import categorydb, languagedb, productdb


# Create your views here.
def indexpage(request):
    return render(request, "indexpage.html")


def addcategory(request):
    return render(request, "addcategory.html")


def categorysave(request):
    if request.method == "POST":
        na = request.POST.get('category')
        obj = categorydb(CategoryName=na)
        obj.save()
        return redirect(addcategory)


def addlanguage(request):
    data = categorydb.objects.all()
    return render(request, "language.html", {'data': data})


def languagesave(request):
    if request.method == "POST":
        la = request.POST.get('language')
        obj = languagedb(Language=la)
        obj.save()
        return redirect(addlanguage)


def addproduct(request):
    data = categorydb.objects.all()
    cat = languagedb.objects.all()
    return render(request, "addproduct.html", {'data': data, 'cat': cat})


def productsave(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        la = request.POST.get('language')
        mov = request.POST.get('movie')
        pr = request.POST.get('price')
        img = request.FILES['thumb']
        obj = productdb(CategoryName=ca, Language=la, MovieName=mov, Price=pr, Thumbnail=img)
        obj.save()
        return redirect(addproduct)


def displayproduct(request):
    data = productdb.objects.all()
    return render(request, "displayproducts.html", {'data': data})


def editproduct(request, dataid):
    data = categorydb.objects.all()
    cat = languagedb.objects.all()
    li = productdb.objects.get(id=dataid)
    return render(request, "editproduct.html", {'li': li, 'data': data, 'cat': cat})


def updatemov(req, dataid):
    if req.method == "POST":
        ca = req.POST.get('category')
        la = req.POST.get('language')
        mov = req.POST.get('movie')
        pr = req.POST.get('price')
        try:
            img = req.FILES['thumb']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Thumbnail
        productdb.objects.filter(id=dataid).update(CategoryName=ca, Language=la, MovieName=mov, Price=pr,
                                                   Thumbnail=file)
        return redirect(displayproduct)


def deleteproduct(request, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def adminlogin(request):
    return render(request, "adminlogin.html")


def adminsave(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                return redirect(addproduct)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)
