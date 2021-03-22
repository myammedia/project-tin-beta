from django.contrib.sitemaps import Sitemap
from youtuber.models import Profile


class YoutuberProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Profile.objects.all()

    def lastmod(self, obj):
        return obj.pub_date