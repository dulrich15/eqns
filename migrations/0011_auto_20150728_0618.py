# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0010_auto_20150703_0623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constant',
            options={'ordering': ['name', 'symbol']},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['symbol', 'name']},
        ),
        migrations.AlterModelOptions(
            name='variable',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='constant',
            name='unit',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='constant',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
