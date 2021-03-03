from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image_png = models.ImageField(blank=True, upload_to='images/category')
    image_svg = models.FileField(blank=True, upload_to='images/category')

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
