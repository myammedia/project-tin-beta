from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber


def index(request):
    template = 'top_five/top-five-index.html'

    return render(request, template)


def youtuber_category_view(request):
    youtuber_category_list = Channel.objects.order_by('name')
    context = {'youtuber_category_list': youtuber_category_list}
    template = 'top_five/top-five-youtuber-category.html'

    return render(request, template, context)


def youtuber_subscat_view(request, slug):
    channel_category = get_object_or_404(Channel, slug=slug)
    context = {'channel_category': channel_category}
    template = "top_five/top-five-youtuber-subscat.html"

    return render(request, template, context)
