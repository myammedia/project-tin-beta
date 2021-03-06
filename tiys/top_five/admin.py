from django.contrib import admin
from . models import Channels, Youtubers


class ChannelAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('channel_category', 'subscriber_category',)
    list_filter = ('channel_category', 'subscriber_category', 'type',)
    prepopulated_fields = {'first_yt_slug': ('first_yt_name',),
                           'second_yt_slug': ('second_yt_name',),
                           'third_yt_slug': ('third_yt_name',),
                           'fourth_yt_slug': ('fourth_yt_name',),
                           'fifth_yt_slug': ('fifth_yt_name',),
                           }


admin.site.register(Channels, ChannelAdmin)


class YoutuberAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('channel_category', 'subscriber_category',)
    list_filter = ('channel_category', 'subscriber_category', 'date',)


admin.site.register(Youtubers, YoutuberAdmin)

