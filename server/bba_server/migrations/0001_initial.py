# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('lowest_price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Watcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'red', max_length=16, choices=[(0, b'OOS'), (1, b'EXPENSIVE'), (2, b'CHEAP'), (3, b'BUY')])),
                ('purchase', models.BooleanField(default=False)),
                ('target_price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='watcher',
            field=models.ForeignKey(to='bba_server.Watcher'),
        ),
    ]
