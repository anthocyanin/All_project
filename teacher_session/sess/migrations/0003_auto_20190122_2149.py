# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sess', '0002_auto_20190122_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='room',
            field=models.CharField(max_length=30),
        ),
    ]
