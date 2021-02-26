from django.shortcuts import render


def index(request):
    template = 'pages/home.html'

    return render(request, template)
