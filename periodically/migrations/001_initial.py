# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_id', models.CharField(max_length=255)),
                ('schedule_id', models.CharField(max_length=32)),
                ('scheduled_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('completed_successfully', models.BooleanField(default=False)),
                ('is_fake', models.BooleanField(default=False)),
            ],
        ),
    ]
