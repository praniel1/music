# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
    ]
