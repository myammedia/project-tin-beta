from django.contrib import admin
from . models import ChannelProfile, Subsdata


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name',)
    prepopulated_fields = {'slug': ('channel_name',)}


class SubsdataAdmin(admin.ModelAdmin):
    list_display = ('get_channel', 'total_subs', 'total_videos', 'total_views',)

    def get_channel(self, obj):
        return obj.profile_subsdata.channel_name

    get_channel.admin_order_field = 'Profile'
    get_channel.short_description = 'Channel Name'


admin.site.register(ChannelProfile, ChannelAdmin)
admin.site.register(Subsdata, SubsdataAdmin)
