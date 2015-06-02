# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0004_remove_cardapio_prep_r11'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepara',
            name='cor',
            field=models.IntegerField(default=1, verbose_name=1),
        ),
    ]
