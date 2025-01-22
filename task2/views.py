from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index1(requests):
    return render(requests, 'games.html')

class index2(TemplateView):
    template_namae = 'cart.html'