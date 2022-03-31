from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
# def authentication(request):
#     return render(request, 'register/register.html')

"""class VAuthentication(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request, 'register/register.html',{'form':form})

    def post(self,request):
        pass
"""


def registerPage(request):
    form = CreateUserForm() # form = UserCreationForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST) # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form':form}
    return render(request, 'authentication/register.html', context)


def Log_in(request):
    context={}
    return render(request, 'authentication/login.html', context)