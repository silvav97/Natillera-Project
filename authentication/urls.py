from django.urls import path
from .views import VAuthentication
# from .import views

urlpatterns = [

    # path('', views.authentication, name='Authentication'),
    # path('', VAuthentication.as_view(), name='Authentication'),
    path('', VAuthentication, name='Authentication'),

    

]