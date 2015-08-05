# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ongoingProjects', '0002_auto_20150804_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='colaborators',
            field=models.ManyToManyField(related_name='Colab', to='ongoingProjects.Human', blank=True),
        ),
    ]
