from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class TopFiveSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['top-five-index', 'top-five-channel-category',
                'top-five-youtuber-category']

    def location(self, item):
        return reverse(item)





