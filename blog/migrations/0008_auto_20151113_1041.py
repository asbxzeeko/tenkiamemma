# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_fileupload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileUpload',
            new_name='File',
        ),
    ]
