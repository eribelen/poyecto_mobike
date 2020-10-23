from django.db import models
from django.shortcuts import render

# Create your models here.
def home(request):
    return render(request, 'Mobike/home.html', {})