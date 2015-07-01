# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order', 'name'],
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('value', models.FloatField()),
            ],
            options={
                'ordering': ['symbol'],
            },
        ),
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sympy', models.TextField()),
                ('latex', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(to='eqns.Category')),
                ('constants', models.ManyToManyField(to='eqns.Constant', blank=True)),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('quantity', models.CharField(max_length=200, null=True, blank=True)),
                ('equivalent', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['symbol'],
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('unit', models.ForeignKey(blank=True, to='eqns.Unit', null=True)),
            ],
            options={
                'ordering': ['symbol'],
            },
        ),
        migrations.AddField(
            model_name='equation',
            name='variables',
            field=models.ManyToManyField(to='eqns.Variable', blank=True),
        ),
        migrations.AddField(
            model_name='constant',
            name='unit',
            field=models.ForeignKey(blank=True, to='eqns.Unit', null=True),
        ),
    ]
