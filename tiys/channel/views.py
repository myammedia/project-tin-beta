from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber


def index(request):
    channel_category_list = Channel.objects.order_by('name')
    context = {'channel_category_list': channel_category_list}
    template = 'channel/channel-index.html'

    return render(request, template, context)
