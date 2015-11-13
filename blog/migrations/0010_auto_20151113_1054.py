# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_file_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploader',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
