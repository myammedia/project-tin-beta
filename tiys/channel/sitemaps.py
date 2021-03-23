from django.contrib.sitemaps import Sitemap
from . models import ChannelProfile


class ChannelProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ChannelProfile.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return '/channel/%s' % obj.slug
