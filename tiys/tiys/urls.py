from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import PagesSitemap
from channel.sitemaps import ChannelProfileSitemap
from youtuber.sitemaps import YoutuberProfileSitemap
from top_five.sitemaps import TopFiveSitemap


sitemaps = {
    'pages': PagesSitemap,
    'channel': ChannelProfileSitemap,
    'youtuber': YoutuberProfileSitemap,
    'top_five': TopFiveSitemap,
}

urlpatterns = [
    path('', include('pages.urls')),
    path('youtuber/', include('youtuber.urls')),
    path('channel/', include('channel.urls')),
    path('top-5/', include('top_five.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
