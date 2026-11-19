
from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'django_projet/index.html',context={'date':datetime.now()})