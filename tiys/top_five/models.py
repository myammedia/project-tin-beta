from django.db import models
from category.models import Channel, Subscriber


class Channels(models.Model):
    CHOICES = (
        ('Most Subscribers', 'Most Subscribers'),
        ('Most Videos', 'Most Videos'),
        ('Most Views', 'Most Views'),
    )

    channel_category = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscriber_category = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=CHOICES)
    date = models.DateField()
    first_yt_name = models.CharField(max_length=150)
    first_yt_slug = models.SlugField(max_length=100, unique=True)
    first_yt_data = models.CharField(max_length=150)
    second_yt_name = models.CharField(max_length=150)
    second_yt_slug = models.SlugField(max_length=100, unique=True)
    second_yt_data = models.CharField(max_length=150)
    third_yt_name = models.CharField(max_length=150)
    third_yt_slug = models.SlugField(max_length=100, unique=True)
    third_yt_data = models.CharField(max_length=150)
    fourth_yt_name = models.CharField(max_length=150)
    fourth_yt_slug = models.SlugField(max_length=100, unique=True)
    fourth_yt_data = models.CharField(max_length=150)
    fifth_yt_name = models.CharField(max_length=150)
    fifth_yt_slug = models.SlugField(max_length=100, unique=True)
    fifth_yt_data = models.CharField(max_length=150)


class Youtubers(models.Model):
    CHOICES = (
        ('Most Subscribers', 'Most Subscribers'),
        ('Most Videos', 'Most Videos'),
        ('Most Views', 'Most Views'),
    )

    channel_category = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscriber_category = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=CHOICES)
    date = models.DateField()
    first_yt_name = models.CharField(max_length=150)
    first_yt_slug = models.SlugField(max_length=100, unique=True)
    first_yt_data = models.CharField(max_length=150)
    second_yt_name = models.CharField(max_length=150)
    second_yt_slug = models.SlugField(max_length=100, unique=True)
    second_yt_data = models.CharField(max_length=150)
    third_yt_name = models.CharField(max_length=150)
    third_yt_slug = models.SlugField(max_length=100, unique=True)
    third_yt_data = models.CharField(max_length=150)
    fourth_yt_name = models.CharField(max_length=150)
    fourth_yt_slug = models.SlugField(max_length=100, unique=True)
    fourth_yt_data = models.CharField(max_length=150)
    fifth_yt_name = models.CharField(max_length=150)
    fifth_yt_slug = models.SlugField(max_length=100, unique=True)
    fifth_yt_data = models.CharField(max_length=150)
