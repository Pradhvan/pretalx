# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170225_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='Should be short, only contain lowercase letters and numbers, and must be unique.', validators=[django.core.validators.RegexValidator(message='The slug may only contain letters, numbers, dots and dashes.', regex='^[a-zA-Z0-9.-]+$')], verbose_name='Short form'),
        ),
    ]
