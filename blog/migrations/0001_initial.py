# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=100)),
                ('hero_img', models.CharField(max_length=200)),
                ('secondary_img', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name=__builtin__.max)),
                ('is_published', models.BooleanField(verbose_name=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
