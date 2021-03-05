# Generated by Django 3.1.7 on 2021-03-05 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('channel_owner', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/youtuber')),
                ('join_date', models.DateField()),
                ('first_upload', models.DateField()),
                ('youtube_url', models.URLField()),
                ('instagram_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('channel_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.channel')),
                ('subscriber_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Subsdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_subs', models.CharField(max_length=20)),
                ('total_videos', models.IntegerField()),
                ('total_views', models.IntegerField()),
                ('update_date', models.DateField(auto_now_add=True)),
                ('profile_subsdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtuber.profile')),
            ],
        ),
    ]
