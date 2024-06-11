from django.urls import path
from food.views import *
app_name='food'
urlpatterns=[
    path('chickenbiriyani/',chickenbiriyani,name='chickenbiriyani'),
    path('rasgola/',rasgola,name='rasgola'),
]