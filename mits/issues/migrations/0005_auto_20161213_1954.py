# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_issue_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-index']},
        ),
    ]
