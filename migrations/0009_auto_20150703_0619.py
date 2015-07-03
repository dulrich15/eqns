# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0008_auto_20150703_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constant',
            name='value',
            field=models.FloatField(help_text='Leave blank for constitutive constants', null=True, blank=True),
            preserve_default=True,
        ),
    ]
