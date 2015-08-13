# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0009_auto_20150809_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradenotes',
            name='trade',
            field=models.ForeignKey(related_name='tradenotes', to='fxcm.ClosedTrade'),
        ),
    ]
