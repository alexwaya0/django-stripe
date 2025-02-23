from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "products/home.html")


def success(request):
    return render(request, "products/success.html")


def cancel(request):
    return render(request, "products/cancel.html")