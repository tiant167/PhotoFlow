# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20141125_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstract',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
