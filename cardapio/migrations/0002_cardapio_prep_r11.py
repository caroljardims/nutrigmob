# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio_prep',
            name='r11',
            field=models.IntegerField(default=0, verbose_name=1),
        ),
    ]
