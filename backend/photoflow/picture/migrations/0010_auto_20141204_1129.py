# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0009_picture_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='img_height',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='img_width',
        ),
        migrations.AddField(
            model_name='picture',
            name='thumbnail',
            field=models.ImageField(default='123', upload_to=b'static/images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(upload_to=b'static/images'),
            preserve_default=True,
        ),
    ]
