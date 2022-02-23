from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def definition(request):
    return render(request, 'definition.html')

def weare(request):
    return render(request, 'weare.html')