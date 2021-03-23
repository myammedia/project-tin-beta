from django.db import models

from category.models import Channel, Subscriber


class ChannelProfile(models.Model):
    channel_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    channel_owner = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to='images/channel')
    channel_category = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscriber_category = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    join_date = models.DateField()
    first_upload = models.DateField()
    youtube_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    facebook_url = models.URLField(max_length=200, blank=True)
    website_url = models.URLField(max_length=200, blank=True)
    pub_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.channel_name


class Subsdata(models.Model):
    profile_subsdata = models.ForeignKey(ChannelProfile, on_delete=models.CASCADE)
    total_subs = models.CharField(max_length=20)
    total_videos = models.IntegerField()
    total_views = models.IntegerField()
    update_date = models.DateField(auto_now_add=True, blank=True)
