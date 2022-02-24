from django.urls import path
from .views import create_natillera
# from .import views

urlpatterns = [

    path('', create_natillera, name='create_natillera'),

]