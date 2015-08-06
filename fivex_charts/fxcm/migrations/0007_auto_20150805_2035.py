# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0006_auto_20150805_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedtrade',
            name='ticket',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='closedtrade',
            unique_together=set([('user', 'ticket')]),
        ),
    ]
