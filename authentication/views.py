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

def VAuthentication(request):
    # form = UserCreationForm()
    form = CreateUserForm()

    if request.method=='POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'authentication/register.html', context)