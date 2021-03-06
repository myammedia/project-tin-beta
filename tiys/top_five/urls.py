from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="top-five-index"),
    path('youtuber/', views.youtuber_category_view, name="top-five-youtuber-category"),

]
