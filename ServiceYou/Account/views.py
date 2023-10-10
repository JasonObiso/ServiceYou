from django.shortcuts import render

from django.shortcuts import render
from form import AccountForm

# Create your views here.
def account_login(request):
    return render(request,'account_login.html',)
def account_register(request):
    return render(request,'account_register.html',{'form':AccountForm})
