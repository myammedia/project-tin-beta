from django.db import models
from django.utils.timezone import now


class Submit(models.Model):
    channel_name = models.CharField(max_length=150, unique=True)
    youtube_url = models.URLField(max_length=200, unique=True)
    date = models.DateField(default=now,)

    def __str__(self):
        return self.channel_name
