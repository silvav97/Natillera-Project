from django.shortcuts import render, redirect

from natillera_account.models import Natillera
from .forms import NatilleraCreateForm

# Create your views here.


def natillera_list(request):
    # natilleras = Natillera.objects.all()
    natilleras = Natillera.objects.filter(user=request.user)
    context={'natilleras':natilleras}
    return render(request, 'natillera_account/natillera_list.html', context)


# def natillera_create(request):
#     context={}
#     return render(request, 'natillera_account/natillera_create.html', context)


def natillera_create(request):
    # def get(self, request, *args, **kwargs):
    if request.method=='GET':
        form = NatilleraCreateForm()
        context={'form':form}
        return render(request, 'natillera_account/natillera_create.html', context)

    # def post(self, request, *args, **kwargs):
    if request.method=='POST':
        if request.method=="POST":
            form = NatilleraCreateForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                monthlyfee = form.cleaned_data.get('monthlyfee')

                natillera, created = Natillera.objects.get_or_create(name=name, monthlyfee=monthlyfee, user=request.user)
                natillera.save()
                return redirect('natillera_list')

        context={}
        return render(request, 'natillera_account/natillera_create.html', context)


def natillera_detail(request, pk):
    natillera = Natillera.objects.all()
    natillera = Natillera.objects.filter(id=pk)
    context={'natillera':natillera}
    # context = {}
    return render(request, 'natillera_account/natillera_detail.html', context)
