
from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', home, name='home'),
    path('definition', definition, name='definition'),
    path('whoweare', weare, name='weare'),

]