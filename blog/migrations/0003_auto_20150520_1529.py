# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150520_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='hero_img',
            field=models.ImageField(upload_to=b'hero_images'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='secondary_img',
            field=models.ImageField(upload_to=b'hero_images', blank=True),
        ),
    ]
