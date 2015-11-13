# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.CharField(default='http://i.imgur.com/tkQkOmv.png', max_length=140),
            preserve_default=False,
        ),
    ]
