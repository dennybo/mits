# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_description'),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
            preserve_default=False,
        ),
    ]
