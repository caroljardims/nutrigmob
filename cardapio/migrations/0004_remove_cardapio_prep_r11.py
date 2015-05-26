# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0003_auto_20150526_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardapio_prep',
            name='r11',
        ),
    ]
