from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Place


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result': obj})



