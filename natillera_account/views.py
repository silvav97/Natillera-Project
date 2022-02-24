from multiprocessing import context
from django.shortcuts import render

from natillera_account.models import Natillera

# Create your views here.


def create_natillera(request):
    natilleras = Natillera.objects.all()
    context={'natilleras':natilleras}
    return render(request, 'natillera_account/create_natillera.html', context)