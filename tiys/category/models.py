from django.db import models
from tiys.tiys.storage_backends import MediaStorage


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image_png = models.ImageField(blank=True, storage=MediaStorage())
    image_svg = models.FileField(blank=True, storage=MediaStorage())

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
