from django.contrib import admin

from . models import Channel, Subscriber


class ChannelAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
