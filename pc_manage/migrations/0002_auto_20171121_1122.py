# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmenttype',
            name='comments',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]