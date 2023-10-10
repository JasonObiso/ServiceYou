from django.shortcuts import render

# Create your views here.
def customer_request(request):
    return render(request,'customer_request.html',)

def accept_request(request):
    return render(request,'customer_request.html',)
