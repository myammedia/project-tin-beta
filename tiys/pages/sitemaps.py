from django.contrib import sitemaps
from django.urls import reverse


class PagesSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['homepage', 'about-page', 'contact-page', 'submit-page', 'terms-page', 'privacy-page', 'faq-page',
                'channel-index', 'youtuber-index', 'top-five-index', 'top-five-channel-category',
                'top-five-youtuber-category']

    def location(self, item):
        return reverse(item)
