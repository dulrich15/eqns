# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqns', '0005_auto_20150630_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order', 'name'],
            },
        ),
        migrations.RemoveField(
            model_name='context',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='context',
            name='system',
        ),
        migrations.AlterModelOptions(
            name='equation',
            options={'ordering': ['subject', 'system', 'name']},
        ),
        migrations.RemoveField(
            model_name='equation',
            name='context',
        ),
        migrations.AddField(
            model_name='equation',
            name='subject',
            field=models.ForeignKey(default=1, to='eqns.Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equation',
            name='system',
            field=models.ForeignKey(default=1, to='eqns.System'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Context',
        ),
        migrations.AddField(
            model_name='equation',
            name='limitations',
            field=models.ManyToManyField(to='eqns.Limitation', blank=True),
        ),
    ]
