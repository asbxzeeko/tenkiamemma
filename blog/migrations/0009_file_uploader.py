# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20151113_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='uploader',
            field=models.ForeignKey(default='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
