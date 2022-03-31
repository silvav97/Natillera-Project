from distutils.log import Log
from django.urls import path
from .views import registerPage, Log_in
# from .import views

urlpatterns = [

    # path('', views.authentication, name='Authentication'),
    # path('', VAuthentication.as_view(), name='Authentication'),
    path('register/', registerPage, name='Authentication'),
    path('login/', Log_in, name='Log_in'),

    

]