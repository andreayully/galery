# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-05 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0006_auto_20190204_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.RemoveField(
            model_name='photopost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='photopost',
            name='photoInfo',
        ),
        migrations.DeleteModel(
            name='PhotoInfo',
        ),
        migrations.DeleteModel(
            name='PhotoPost',
        ),
        migrations.DeleteModel(
            name='RelatedPhoto',
        ),
    ]
