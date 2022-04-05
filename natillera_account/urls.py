from django.urls import path
from .views import natillera_list, natillera_create, natillera_detail
# from .import views

urlpatterns = [

    path('', natillera_list, name='natillera_list'),
    path('create/', natillera_create, name='natillera_create'),
    path('detail/<int:pk>', natillera_detail, name='natillera_detail'),


]