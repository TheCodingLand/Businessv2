# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0012_auto_20171211_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='facebook',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='instagram',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='text1',
            field=models.CharField(default=1, max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='text2',
            field=models.CharField(default=1, max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='twitter',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
