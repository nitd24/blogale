# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150520_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(),
        ),
    ]
