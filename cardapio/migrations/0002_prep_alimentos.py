# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prep_Alimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=40)),
                ('alimento', models.ForeignKey(to='cardapio.Alimentos', to_field='id')),
                ('prep', models.ForeignKey(to='cardapio.Prepara', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
