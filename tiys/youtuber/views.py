from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber


def index(request):
    youtuber_category_list = Channel.objects.order_by('name')
    context = {'youtuber_category_list': youtuber_category_list}
    template = 'youtuber/youtuber-index.html'

    return render(request, template, context)

