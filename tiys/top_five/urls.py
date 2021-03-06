from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="top-five-index"),
    path('youtuber/', views.youtuber_category_view, name="top-five-youtuber-category"),
    path('youtuber/<slug:slug>/', views.youtuber_subscat_view, name="top-five-youtuber-subscat"),
    path('youtuber/<slug:channel_category>/<slug:subscriber_category>/', views.top_five_youtuber_view,
         name="top-five-youtuber-list"),
    path('youtuber/<slug:channel_category>/<slug:subscriber_category>/archives', views.top_five_youtuber_view,
         name="top-five-youtuber-archives"),

]
