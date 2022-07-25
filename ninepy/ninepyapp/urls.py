from django.urls import path, include
from .views import *

urlpatterns =[
path('', SerialVieww.as_view(), name = 'home')

]
