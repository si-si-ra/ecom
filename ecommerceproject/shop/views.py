from django.shortcuts import render
from . models import Products
# from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def product_list(request):
    products=Products.objects.all()
    return render(request,'product_list.html',{'products': products})

def cart(request):
     context={
         'electronics':['Mobile phone','laptop','printers','tv'],
    }
     return render(request,"cart.html",context)

def profile(request):
     return render(request,"profile.html")

def payment(request):
     return render(request,"payment.html")

# Create your views here.
