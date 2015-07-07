# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bba_server', '0002_auto_20150707_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='watcher',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watcher',
            name='status',
            field=models.CharField(default=b'EXPENSIVE', max_length=16, choices=[(0, b'OOS'), (1, b'EXPENSIVE'), (2, b'CHEAP'), (3, b'BUY')]),
        ),
    ]
