# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_auto_20171115_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
