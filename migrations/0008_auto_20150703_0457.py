# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0007_auto_20150703_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='system',
            field=models.ForeignKey(blank=True, to='eqns.System', null=True),
            preserve_default=True,
        ),
    ]
