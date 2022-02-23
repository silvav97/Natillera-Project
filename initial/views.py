from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'initial/home.html')

def definition(request):
    return render(request, 'initial/definition.html')

def weare(request):
    return render(request, 'initial/weare.html')