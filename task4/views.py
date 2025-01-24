from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def welcome(requests):
    return render(requests, 'index.html')


def cart(requests):
    return render(requests, 'cart.html')


def games(requests):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
    return render(requests, 'games.html', context)


def platform(requests):
    return render(requests, 'platform.html')