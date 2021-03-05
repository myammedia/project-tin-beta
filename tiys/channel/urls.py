from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="channel-index"),
    path('<slug:slug>/', views.subscat_list_view, name="channel-subscat-list"),
    path('<slug:channel_category>/<slug:subscriber_category>/', views.channel_list_view,
         name="channel-list"),
    path('<slug:channel_category>/<slug:subscriber_category>/<slug:slug>',
         views.channel_profile_view, name="channel-profile")
]
