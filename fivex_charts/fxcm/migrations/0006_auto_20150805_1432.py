# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0005_auto_20150804_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedtrade',
            name='ticket',
            field=models.IntegerField(unique=True),
        ),
    ]
