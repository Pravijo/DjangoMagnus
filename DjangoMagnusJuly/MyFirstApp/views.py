from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .models import Pets
from .forms import UserForm, EmpForm

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


def emp(request):
    emp_data = Employee.objects.all()
    data = {"Employee":emp_data}
    return render(request,'MyFirstApp/Emp.html',context=data)


def pet(request):
    pet_data = Pets.objects.all()
    data = {"Pets":pet_data}
    return render(request,'MyFirstApp/Pet.html',context=data)


def form_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
    return render(request,'MyFirstApp/UserForm.html',{'form':form})


def emp_formpage(request):
    form = EmpForm()
    if request.method=='POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Inserted Successfully</h1>")
        else:
            return HttpResponse("<h1>Invalid Details</h1>")
    return render(request,'MyFirstApp/EmpForm.html',{'form':form})