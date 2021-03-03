from django.contrib import admin
from . models import Profile, Subsdata


class YoutuberAdmin(admin.ModelAdmin):
    list_display = ('channel_name',)
    prepopulated_fields = {'slug': ('channel_name',)}


class SubsdataAdmin(admin.ModelAdmin):
    list_display = ('get_youtuber', 'total_subs', 'total_videos', 'total_views',)

    def get_youtuber(self, obj):
        return obj.profile_subsdata.channel_name

    get_youtuber.admin_order_field = 'Profile'
    get_youtuber.short_description = 'Channel Name'


admin.site.register(Profile, YoutuberAdmin)
admin.site.register(Subsdata, SubsdataAdmin)
