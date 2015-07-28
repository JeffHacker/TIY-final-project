# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedTrades',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ticket', models.IntegerField()),
                ('symbol', models.CharField(max_length=7)),
                ('volume', models.IntegerField()),
                ('opendatetime', models.DateTimeField()),
                ('closedatetime', models.DateTimeField()),
                ('soldprice', models.DecimalField(decimal_places=5, max_digits=10)),
                ('boughtprice', models.DecimalField(decimal_places=5, max_digits=10)),
                ('direction', models.CharField(max_length=5)),
                ('grossprofitloss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dividends', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rollover', models.DecimalField(decimal_places=2, max_digits=10)),
                ('adj', models.DecimalField(decimal_places=2, max_digits=10)),
                ('netprofitloss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buycondition', models.CharField(max_length=3)),
                ('sellcondition', models.CharField(max_length=3)),
                ('createdbyaccount', models.IntegerField()),
                ('journal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('member', models.BooleanField(default=False)),
                ('administrator', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='closedtrades',
            name='user',
            field=models.ForeignKey(to='fxcm.UserProfile'),
        ),
    ]
