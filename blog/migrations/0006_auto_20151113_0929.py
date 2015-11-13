# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='example@example.com', max_length=1024),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
