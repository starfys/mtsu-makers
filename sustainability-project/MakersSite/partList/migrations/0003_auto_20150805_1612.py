# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partList', '0002_auto_20150805_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='inProject',
            field=models.BooleanField(default=b''),
        ),
    ]
