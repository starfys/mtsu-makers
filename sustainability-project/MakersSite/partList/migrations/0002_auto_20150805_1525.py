# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='inProject',
            field=models.TextField(default=b''),
        ),
    ]
