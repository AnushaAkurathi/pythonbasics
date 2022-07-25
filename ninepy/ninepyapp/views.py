from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import Questions_serial
from .models import Questions
# Create your views here.



def HomeView(request):
    return HttpResponse('Hi welcome to the website!!!')


class SerialVieww(ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = Questions_serial
