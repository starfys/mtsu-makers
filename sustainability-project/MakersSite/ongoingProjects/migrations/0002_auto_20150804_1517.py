# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ongoingProjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='colaborators',
        ),
        migrations.RemoveField(
            model_name='project',
            name='partsList',
        ),
        migrations.AddField(
            model_name='project',
            name='colaborators',
            field=models.ManyToManyField(related_name='Colaborators', to='ongoingProjects.Human', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='partsList',
            field=models.ManyToManyField(related_name='Part_List', to='ongoingProjects.Parts', blank=True),
        ),
    ]
