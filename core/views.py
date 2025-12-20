from django.shortcuts import render
from django.http import HttpResponse
from .models import Campeao
# Create your views here.


def home(request):
    campeoes = Campeao.objects.all()
    return render(request, 'core/home.html', {
        'campeoes': campeoes
    })
