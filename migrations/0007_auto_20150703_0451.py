# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0006_auto_20150701_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constant',
            name='unit',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
