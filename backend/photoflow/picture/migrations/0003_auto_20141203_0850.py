# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_auto_20141203_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(height_field=b'img_height', width_field=b'img_width', upload_to=b''),
            preserve_default=True,
        ),
    ]
