from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('about-us', views.about, name="about-page"),
    path('contact-us', views.contact, name="contact-page"),
]
