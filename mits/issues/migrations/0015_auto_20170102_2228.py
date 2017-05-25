# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0014_auto_20161220_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='issues.Event')),
                ('pinned', models.BooleanField(default=False)),
            ],
            bases=('issues.event',),
        ),
        migrations.AddField(
            model_name='issue',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]