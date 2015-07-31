# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0002_auto_20150729_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedtrades',
            name='createdbyaccount',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='closedtrades',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='uploadeddata',
            name='data',
            field=models.FileField(upload_to='csv_data/%Y/%m/%d'),
        ),
    ]
