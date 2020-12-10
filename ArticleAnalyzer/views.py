from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'home': 'Home Page'})


def result(request):
    article = request.GET['article']
    return render(request, 'result.html', {'article': article})
