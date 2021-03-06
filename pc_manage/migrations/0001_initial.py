# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=256)),
                ('sn', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('comments', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('comments', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_manage.DepartmentType')),
            ],
        ),
        migrations.AddField(
            model_name='computerinfo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_manage.ComputerType'),
        ),
    ]
