# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0005_auto_20150602_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardapio_prep',
            old_name='r3_1',
            new_name='r3',
        ),
        migrations.RemoveField(
            model_name='cardapio_prep',
            name='r3_2',
        ),
    ]
