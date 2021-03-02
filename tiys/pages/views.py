from django.shortcuts import render
from .forms import SubmitForm


def index(request):
    template = 'pages/home.html'

    return render(request, template)


def about(request):
    # category_list = Channel.objects.order_by('name')
    # subscriber_list = Subscriber.objects.all()
    # context = {'category_list': category_list, 'subscriber_list': subscriber_list}
    template = 'pages/about.html'

    return render(request, template)


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