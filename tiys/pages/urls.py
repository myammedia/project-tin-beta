from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('about-us', views.about, name="about-page"),
]
