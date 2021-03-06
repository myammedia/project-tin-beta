# Generated by Django 3.1.7 on 2021-03-06 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtubers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Most Subscribers', 'Most Subscribers'), ('Most Videos', 'Most Videos'), ('Most Views', 'Most Views')], max_length=50)),
                ('date', models.DateField()),
                ('first_yt_name', models.CharField(max_length=150)),
                ('first_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('first_yt_data', models.CharField(max_length=150)),
                ('second_yt_name', models.CharField(max_length=150)),
                ('second_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('second_yt_data', models.CharField(max_length=150)),
                ('third_yt_name', models.CharField(max_length=150)),
                ('third_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('third_yt_data', models.CharField(max_length=150)),
                ('fourth_yt_name', models.CharField(max_length=150)),
                ('fourth_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('fourth_yt_data', models.CharField(max_length=150)),
                ('fifth_yt_name', models.CharField(max_length=150)),
                ('fifth_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('fifth_yt_data', models.CharField(max_length=150)),
                ('channel_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.channel')),
                ('subscriber_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Most Subscribers', 'Most Subscribers'), ('Most Videos', 'Most Videos'), ('Most Views', 'Most Views')], max_length=50)),
                ('date', models.DateField()),
                ('first_yt_name', models.CharField(max_length=150)),
                ('first_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('first_yt_data', models.CharField(max_length=150)),
                ('second_yt_name', models.CharField(max_length=150)),
                ('second_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('second_yt_data', models.CharField(max_length=150)),
                ('third_yt_name', models.CharField(max_length=150)),
                ('third_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('third_yt_data', models.CharField(max_length=150)),
                ('fourth_yt_name', models.CharField(max_length=150)),
                ('fourth_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('fourth_yt_data', models.CharField(max_length=150)),
                ('fifth_yt_name', models.CharField(max_length=150)),
                ('fifth_yt_slug', models.SlugField(max_length=100, unique=True)),
                ('fifth_yt_data', models.CharField(max_length=150)),
                ('channel_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.channel')),
                ('subscriber_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subscriber')),
            ],
        ),
    ]