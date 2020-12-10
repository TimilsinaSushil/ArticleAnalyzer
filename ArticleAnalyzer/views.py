from . import counter

from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'home': 'Home Page'})


def result(request):
    article = request.GET['article']
    words, word_count = counter.count(article);
    return render(request, 'result.html', {'article': article, 'word_count': word_count, 'words': words})
