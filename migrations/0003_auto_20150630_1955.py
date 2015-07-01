# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0002_auto_20150630_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='context',
            options={'ordering': ['category', 'sort_order', 'name']},
        ),
        migrations.AlterModelOptions(
            name='equation',
            options={'ordering': ['context', 'name']},
        ),
        migrations.RemoveField(
            model_name='equation',
            name='category',
        ),
        migrations.AddField(
            model_name='context',
            name='category',
            field=models.ForeignKey(default=1, to='eqns.Category'),
            preserve_default=False,
        ),
    ]
