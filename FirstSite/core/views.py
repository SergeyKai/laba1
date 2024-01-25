from django.shortcuts import render

from .models import Film


def index(request):
    return render(request, 'core/base.html')


def film_list(request):
    films = Film.objects.all()
    return render(request, 'core/film_list.html', context={'film_list': films})


def film_detail(request, pk):
    film = Film.objects.get(pk=pk)
    return render(request, 'core/film_detail.html', context={'film': film})
