# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_auto_20180717_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='image',
            field=models.ImageField(default=1234, upload_to='category/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(default=1234, upload_to='location/'),
            preserve_default=False,
        ),
    ]