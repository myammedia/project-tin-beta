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


def channel_list_view(request, channel_category, subscriber_category):
    channel_category = Channel.objects.get(slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    channel_list = ChannelProfile.objects.filter(channel_category=channel_category,
                                                 subscriber_category=subscriber_category)
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'channel_list': channel_list}
    template = 'channel/channel-list.html'

    return render(request, template, context)
