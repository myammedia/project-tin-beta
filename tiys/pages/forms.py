from django.forms import ModelForm
from .models import Submit


class SubmitForm(ModelForm):
    class Meta:
        model = Submit
        fields = [
            'channel_name', 'youtube_url'
        ]
