# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0007_auto_20150805_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='closedtrade',
            name='tradenotes',
            field=models.TextField(blank=True, help_text='Trade Notes:'),
        ),
    ]
