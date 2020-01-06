from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app(request):
 #   return HttpResponse("<h1>Hello World</h1>")
 #   return render(request , "index.html")
 #   a = input("Enter Your Name")
     return render(request , "home.html" , {"name" : "Taha Naviwala"})


def con(request):
#   b = input("Enter Contact No")
    return render(request , "contact.html" , {"contact" : "03302843162"})


def add(request):
    val1 = request.GET["num1"]
    val2 = request.GET["num2"]
    total  = int(val1) + int(val2)
    return render(request , "result.html" , {"result":total})
