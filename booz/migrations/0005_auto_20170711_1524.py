# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booz', '0004_auto_20170711_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booz',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='public or private'),
        ),
    ]
