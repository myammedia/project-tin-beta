from django.shortcuts import render
from category.models import Channel, Subscriber
from channel.models import ChannelProfile
from youtuber.models import Profile
from .models import Faq
from .forms import SubmitForm


def index(request):
    channel_category_count = Channel.objects.count()
    subscriber_category_count = Subscriber.objects.count()
    youtuber_count = Profile.objects.count()
    channel_count = ChannelProfile.objects.count()
    context = {'channel_category_count': channel_category_count, 'subscriber_category_count': subscriber_category_count,
               'youtuber_count': youtuber_count, 'channel_count': channel_count, }

    template = 'pages/home.html'

    return render(request, template, context)


def about(request):
    category_list = Channel.objects.order_by('name')
    subscriber_list = Subscriber.objects.all()
    context = {'category_list': category_list, 'subscriber_list': subscriber_list}
    template = 'pages/about.html'

    return render(request, template, context)


def contact(request):

    template = 'pages/contact.html'

    return render(request, template)


def privacy(request):
    template = 'pages/privacy.html'

    return render(request, template)


def terms(request):
    template = 'pages/terms.html'

    return render(request, template)


def submit(request):
    form = SubmitForm(request.POST)
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    template = 'pages/submit.html'

    return render(request, template, context)


def faq(request):
    faq_list = Faq.objects.order_by('date')
    context = {'faq_list': faq_list}
    template = 'pages/faq.html'

    return render(request, template, context)
