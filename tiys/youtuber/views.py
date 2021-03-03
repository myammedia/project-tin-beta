from django.shortcuts import render, get_object_or_404
from category.models import Channel, Subscriber
from .models import Profile, Subsdata


def index(request):
    youtuber_category_list = Channel.objects.order_by('name')
    context = {'youtuber_category_list': youtuber_category_list}
    template = 'youtuber/youtuber-index.html'

    return render(request, template, context)


def subscat_list_view(request, slug):
    channel_category = get_object_or_404(Channel, slug=slug)
    context = {'channel_category': channel_category,}
    template = "youtuber/youtuber-subscat.html"

    return render(request, template, context)


def youtuber_list_view(request, channel_category, subscriber_category):
    channel_category = Channel.objects.get(slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    youtuber_list = Profile.objects.filter(channel_category=channel_category, subscriber_category=subscriber_category)
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'youtuber_list': youtuber_list}
    template = 'youtuber/youtuber-list.html'

    return render(request, template, context)


def youtuber_profile_view(request, channel_category, subscriber_category, slug):
    youtuber = Profile.objects.get(slug=slug)
    channel_category = Channel.objects.get(slug=channel_category)
    subscriber_category = Subscriber.objects.get(slug=subscriber_category)
    subsdata = Subsdata.objects.filter(profile_subsdata__slug=slug).last()
    context = {'channel_category': channel_category, 'subscriber_category': subscriber_category,
               'youtuber': youtuber, 'subsdata': subsdata}
    template = 'youtuber/youtuber-profile.html'

    return render(request, template, context)


