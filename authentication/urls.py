from distutils.log import Log
from django.urls import path
from .views import registerPage, loginPage, logoutUser
# from .import views

urlpatterns = [

    # path('', views.authentication, name='Authentication'),
    # path('', VAuthentication.as_view(), name='Authentication'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    

]