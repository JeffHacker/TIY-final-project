# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0008_closedtrade_tradenotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('note', models.TextField(blank=True, help_text='Trade Notes:')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='closedtrade',
            name='tradenotes',
        ),
        migrations.AddField(
            model_name='tradenotes',
            name='trade',
            field=models.ForeignKey(to='fxcm.ClosedTrade'),
        ),
    ]
