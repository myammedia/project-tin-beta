from django.shortcuts import render


def index(request):
    template = 'pages/home.html'

    return render(request, template)


def about(request):
    # category_list = Channel.objects.order_by('name')
    # subscriber_list = Subscriber.objects.all()
    # context = {'category_list': category_list, 'subscriber_list': subscriber_list}
    template = 'pages/about.html'

    return render(request, template)
