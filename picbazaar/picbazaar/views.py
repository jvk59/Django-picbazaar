from tkinter import Image
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
def show_about_page(request):
    print("about page request")
    
    #return HttpResponse("<h1>hi this is about this page</h1>")
    name='Vivek'
    link='https://www.youtube.com'

    data={
        'name': name,
        'link': link
    }
    #return render(request,"about.html",{})
    return render(request,"about.html",data)

def show_home_page(request):
    #load images
    images=Image.objects.all()
    #load categories
    cats=Category.objects.all()
    data={'images':images,'cats':cats}
    
    #return render(request,"home.html",{})
    return render(request,"home.html",data)

def show_category_page(request,cid):
    cats=Category.objects.all()
    categ=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=categ)
    data={'images':images,'cats':cats}
    
    #return render(request,"home.html",{})
    return render(request,"home.html",data)