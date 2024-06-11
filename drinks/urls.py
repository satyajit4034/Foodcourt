from django.urls import path 
from drinks.views import *
app_name = 'drinks'
urlpatterns = [
   path('eno/',eno,name='eno'),
   path('lassi/',lassi,name='lassi'), 
]


