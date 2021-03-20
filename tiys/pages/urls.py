from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('about-us', views.about, name="about-page"),
    path('submit-detail', views.submit, name="submit-page"),
    path('contact-us', views.contact, name="contact-page"),
    path('privacy-policy', views.privacy, name="privacy-page"),
    path('terms-and-conditions', views.terms, name="terms-page"),
    path('faq', views.faq, name="faq-page"),
]
