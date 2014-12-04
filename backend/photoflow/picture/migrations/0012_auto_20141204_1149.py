# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0011_auto_20141204_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='img_height',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='img_width',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(height_field=b'img_height', width_field=b'img_width', upload_to=b'static/images'),
            preserve_default=True,
        ),
    ]
