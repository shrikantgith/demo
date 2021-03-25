from django.shortcuts import render
from .forms import BuyerRegistration
# Create your views here.

def signin(request):
    form =BuyerRegistration()
    if request.method == "POST":
        print("hello")
        return render(request,'dashboard.html')
    return render(request,'signin.html',{'form':form})

def login(request):

    return render(request,'login.html')
def sigsub(request):
    pass
def logsub(request):
    return render(request,'dashboard.html')