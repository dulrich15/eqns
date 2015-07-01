# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0003_auto_20150630_1955'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Subject',
        ),
        migrations.AlterModelOptions(
            name='context',
            options={'ordering': ['subject', 'sort_order', 'name']},
        ),
        migrations.RenameField(
            model_name='context',
            old_name='category',
            new_name='subject',
        ),
    ]
