# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='img_height',
            field=models.PositiveIntegerField(default='800'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='img_width',
            field=models.PositiveIntegerField(default='800'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(height_field=models.PositiveIntegerField(), width_field=models.PositiveIntegerField(), upload_to=b''),
            preserve_default=True,
        ),
    ]
