# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='abstract',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
