from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    data = {"name":"Valli"}
    return render(request,'MyFirstApp/Home.html',context=data)
    # return HttpResponse("<h1>Welcome to Django</h1>")


def help(request):
    return HttpResponse("<h1>Help Page</h1>")


def welcome(request):
    return HttpResponse("<h1>Welcome to the World</h1>")


def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")
