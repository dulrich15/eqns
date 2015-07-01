# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0004_auto_20150630_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order', 'name'],
            },
        ),
        migrations.AlterModelOptions(
            name='context',
            options={'ordering': ['subject', 'system', 'sort_order']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['sort_order', 'name']},
        ),
        migrations.RemoveField(
            model_name='context',
            name='name',
        ),
        migrations.AddField(
            model_name='context',
            name='notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='context',
            name='system',
            field=models.ForeignKey(default=1, to='eqns.System'),
            preserve_default=False,
        ),
    ]
