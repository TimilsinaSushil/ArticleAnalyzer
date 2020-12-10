import operator

from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'home': 'Home Page'})


def result(request):
    article = request.GET['article']
    words = article.split()
    word_count = len(words)
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

        words=sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)  # descending order
    return render(request, 'result.html', {'article': article, 'word_count': word_count, 'words': words})
