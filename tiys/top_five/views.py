from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber
from .models import Channels, Youtubers


def index(request):
    template = 'top_five/top-five-index.html'

    return render(request, template)


def channel_category_view(request):
    channel_category_list = Channel.objects.order_by('name')
    context = {'channel_category_list': channel_category_list}
    template = 'top_five/top-five-channel-category.html'

    return render(request, template, context)


def channel_subscat_view(request, slug):
    channel_category = get_object_or_404(Channel, slug=slug)
    context = {'channel_category': channel_category}
    template = "top_five/top-five-channel-subscat.html"

    return render(request, template, context)


def top_five_channel_view(request, channel_category, subscriber_category):
    channel_category = get_object_or_404(Channel, slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    top_five_subs = Channels.objects.filter(channel_category=channel_category, subscriber_category=subscriber_category,
                                            type='Most Subscribers').last()
    top_five_videos = Channels.objects.filter(channel_category=channel_category, subscriber_category=subscriber_category,
                                              type='Most Videos').last()
    top_five_views = Channels.objects.filter(channel_category=channel_category, subscriber_category=subscriber_category,
                                             type='Most Views').last()
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'top_five_subs': top_five_subs,
               'top_five_videos': top_five_videos, 'top_five_views': top_five_views}
    template = 'top_five/top-five-channel-list.html'

    return render(request, template, context)


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


def top_five_youtuber_view(request, channel_category, subscriber_category):
    channel_category = get_object_or_404(Channel, slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    top_five_subs = Youtubers.objects.filter(channel_category=channel_category,
                                             subscriber_category=subscriber_category, type='Most Subscribers').last()
    top_five_videos = Youtubers.objects.filter(channel_category=channel_category,
                                               subscriber_category=subscriber_category, type='Most Videos').last()
    top_five_views = Youtubers.objects.filter(channel_category=channel_category,
                                              subscriber_category=subscriber_category, type='Most Views').last()
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'top_five_subs': top_five_subs,
               'top_five_videos': top_five_videos, 'top_five_views': top_five_views}
    template = 'top_five/top-five-youtuber-list.html'

    return render(request, template, context)


def top_five_youtuber_archive_view(request, channel_category, subscriber_category):
    channel_category = get_object_or_404(Channel, slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    top_five_archive_list = Youtubers.objects.filter(channel_category=channel_category,
                                                     subscriber_category=subscriber_category)
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'top_five_archive_list': top_five_archive_list}
    template = 'top_five/top-five-youtuber-archive.html'

    return render(request, template, context)
