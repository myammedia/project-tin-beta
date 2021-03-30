from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/images/category')


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image_png = models.ImageField(blank=True, storage=fs)
    image_svg = models.FileField(blank=True, storage=fs)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
