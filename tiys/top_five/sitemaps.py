from django.contrib.sitemaps import Sitemap
from top_five.models import Channels, Youtubers


class TopChannelSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Channels.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class TopYoutuberSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Youtubers.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

