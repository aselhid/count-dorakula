# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171114_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retry',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='top',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
