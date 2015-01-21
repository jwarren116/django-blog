# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120, verbose_name=b'Title')),
                ('post', models.TextField(verbose_name=b'Content')),
                ('blurb', models.TextField(null=True, verbose_name=b'Blurb')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('display', models.BooleanField(default=False, verbose_name=b'Display on Home Page?')),
                ('heading', models.BooleanField(default=False, verbose_name=b'Display as Heading?')),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
            },
            bases=(models.Model,),
        ),
    ]
