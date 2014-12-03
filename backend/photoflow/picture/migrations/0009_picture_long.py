# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0008_auto_20141203_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='long',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
