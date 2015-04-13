# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempHumidity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temphumidity',
            old_name='model',
            new_name='pi_num',
        ),
    ]
