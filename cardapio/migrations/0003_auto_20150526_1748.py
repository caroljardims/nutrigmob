# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_cardapio_prep_r11'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r1',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r10',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r2',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r3_1',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r3_2',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r4',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r5',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r6',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r7',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r8',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
        migrations.AlterField(
            model_name='cardapio_prep',
            name='r9',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
    ]
