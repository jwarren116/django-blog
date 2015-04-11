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
                ('title', models.CharField(max_length=63, verbose_name=b'Title')),
                ('post', models.TextField(verbose_name=b'Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('display', models.BooleanField(default=False, verbose_name=b'Display on Home Page?')),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('screen_shot', models.ImageField(upload_to=b'screen_shots')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('display', models.BooleanField(default=False, verbose_name=b'Display on Home Page?')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
    ]
