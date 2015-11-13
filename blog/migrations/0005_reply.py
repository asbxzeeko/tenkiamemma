# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(null=True, blank=True)),
                ('comment', models.ForeignKey(related_name='replies', to='blog.Comment')),
            ],
        ),
    ]
