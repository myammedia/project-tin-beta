from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber


def index(request):
    channel_category_list = Channel.objects.order_by('name')
    context = {'channel_category_list': channel_category_list}
    template = 'channel/channel-index.html'

    return render(request, template, context)


def subscat_list_view(request, slug):
    channel_category = get_object_or_404(Channel, slug=slug)
    context = {'channel_category': channel_category,}
    template = "channel/channel-subscat.html"

    return render(request, template, context)
