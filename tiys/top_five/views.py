from django.shortcuts import render


def index(request):
    template = 'top_five/top-five-index.html'

    return render(request, template)
