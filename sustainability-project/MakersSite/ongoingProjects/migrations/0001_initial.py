# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ongoingProjects.multivalue


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectName', models.CharField(max_length=64)),
                ('colaborators', ongoingProjects.multivalue.separateValues()),
                ('partsList', ongoingProjects.multivalue.separateValues()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
