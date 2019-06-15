# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-09 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_worker_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date joind')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('resworker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Worker')),
            ],
        ),
    ]
