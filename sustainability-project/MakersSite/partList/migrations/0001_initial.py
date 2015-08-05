# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('brand', models.TextField(default=b'')),
                ('cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('storage', models.TextField(default=b'')),
                ('inProject', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('serialNumber', models.TextField(default=b'')),
            ],
        ),
    ]
