# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fxcm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('data', models.FileField(upload_to='csv_data')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='closedtrades',
            name='journal',
        ),
        migrations.AlterField(
            model_name='closedtrades',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='closedtrades',
            name='data',
            field=models.ForeignKey(to='fxcm.UploadedData', default=1),
            preserve_default=False,
        ),
    ]
