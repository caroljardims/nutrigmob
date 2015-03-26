# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prepara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=40)),
                ('inNatura', models.IntegerField(max_length=1)),
                ('enxofre', models.IntegerField(max_length=1)),
                ('sodio', models.IntegerField(max_length=1)),
                ('cor', models.CharField(max_length=10)),
                ('tipoPrep', models.CharField(max_length=40)),
                ('coccao', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Aux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(max_length=1)),
                ('desc', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dia_Cardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(max_length=2)),
                ('mes', models.IntegerField(max_length=2)),
                ('ano', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=20)),
                ('cat_alimento', models.ForeignKey(to='cardapio.Aux', to_field='id')),
                ('cor', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cardapio_Prep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.ForeignKey(to='cardapio.Dia_Cardapio', to_field='id')),
                ('prep', models.ForeignKey(to='cardapio.Prepara', to_field='id')),
                ('r1', models.IntegerField(max_length=1)),
                ('r2', models.IntegerField(max_length=1)),
                ('r3_1', models.IntegerField(max_length=1)),
                ('r3_2', models.IntegerField(max_length=1)),
                ('r4', models.IntegerField(max_length=1)),
                ('r5', models.IntegerField(max_length=1)),
                ('r6', models.IntegerField(max_length=1)),
                ('r7', models.IntegerField(max_length=1)),
                ('r8', models.IntegerField(max_length=1)),
                ('r9', models.IntegerField(max_length=1)),
                ('r10', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
