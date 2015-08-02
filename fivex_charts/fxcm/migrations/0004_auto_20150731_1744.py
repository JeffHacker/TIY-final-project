# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fxcm', '0003_auto_20150730_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ticket', models.IntegerField()),
                ('symbol', models.CharField(max_length=7)),
                ('volume', models.IntegerField()),
                ('opendatetime', models.DateTimeField()),
                ('closedatetime', models.DateTimeField()),
                ('soldprice', models.DecimalField(max_digits=10, decimal_places=5)),
                ('boughtprice', models.DecimalField(max_digits=10, decimal_places=5)),
                ('direction', models.CharField(max_length=5)),
                ('grossprofitloss', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comm', models.DecimalField(max_digits=10, decimal_places=2)),
                ('dividends', models.DecimalField(max_digits=10, decimal_places=2)),
                ('rollover', models.DecimalField(max_digits=10, decimal_places=2)),
                ('adj', models.DecimalField(max_digits=10, decimal_places=2)),
                ('netprofitloss', models.DecimalField(max_digits=10, decimal_places=2)),
                ('buycondition', models.CharField(max_length=3)),
                ('sellcondition', models.CharField(max_length=3)),
                ('createdbyaccount', models.BigIntegerField()),
                ('data', models.ForeignKey(to='fxcm.UploadedData')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', models.TextField()),
                ('data', models.TextField(db_index=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='closedtrades',
            name='data',
        ),
        migrations.RemoveField(
            model_name='closedtrades',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClosedTrades',
        ),
    ]
