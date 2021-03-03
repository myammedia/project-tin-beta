from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="youtuber-index"),
    path('<slug:slug>/', views.subscat_list_view, name="youtuber-subscat-list"),
    path('<slug:channel_category>/<slug:subscriber_category>/', views.youtuber_list_view,
         name="youtuber-list"),
]
