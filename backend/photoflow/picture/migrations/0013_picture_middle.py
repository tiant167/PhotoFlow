# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0012_auto_20141204_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='middle',
            field=models.ImageField(null=True, upload_to=b'static/images', blank=True),
            preserve_default=True,
        ),
    ]
