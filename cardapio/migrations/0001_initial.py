# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Aux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(verbose_name=1)),
                ('desc', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio_Prep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r1', models.IntegerField(verbose_name=1)),
                ('r2', models.IntegerField(verbose_name=1)),
                ('r3_1', models.IntegerField(verbose_name=1)),
                ('r3_2', models.IntegerField(verbose_name=1)),
                ('r4', models.IntegerField(verbose_name=1)),
                ('r5', models.IntegerField(verbose_name=1)),
                ('r6', models.IntegerField(verbose_name=1)),
                ('r7', models.IntegerField(verbose_name=1)),
                ('r8', models.IntegerField(verbose_name=1)),
                ('r9', models.IntegerField(verbose_name=1)),
                ('r10', models.IntegerField(verbose_name=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dia_Cardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(verbose_name=2)),
                ('mes', models.IntegerField(verbose_name=2)),
                ('ano', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='Prep_Alimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=40)),
                ('alimento', models.ForeignKey(to='cardapio.Alimentos')),
            ],
        ),
        migrations.CreateModel(
            name='Prepara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=40)),
                ('inNatura', models.IntegerField(verbose_name=1)),
                ('enxofre', models.IntegerField(verbose_name=1)),
                ('sodio', models.IntegerField(verbose_name=1)),
                ('cor', models.CharField(max_length=10)),
                ('tipoPrep', models.CharField(max_length=40)),
                ('coccao', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='prep_alimentos',
            name='prep',
            field=models.ForeignKey(to='cardapio.Prepara'),
        ),
        migrations.AddField(
            model_name='cardapio_prep',
            name='dia',
            field=models.ForeignKey(to='cardapio.Dia_Cardapio'),
        ),
        migrations.AddField(
            model_name='cardapio_prep',
            name='prep',
            field=models.ForeignKey(to='cardapio.Prepara'),
        ),
        migrations.AddField(
            model_name='alimentos',
            name='cat_alimento',
            field=models.ForeignKey(to='cardapio.Aux'),
        ),
    ]
