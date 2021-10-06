from django.shortcuts import render
from .models import Donuts

# Create your views here.

def indexPageView(request):
    context = {'donuts':Donuts.objects.all()}
    return render(request, 'homepage/index.html', context)