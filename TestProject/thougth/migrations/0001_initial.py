# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 22:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('conditions', models.IntegerField(choices=[(1, 'Joy'), (5, 'Passionate'), (10, 'Happy'), (15, 'Positive'), (20, 'Content'), (25, 'Bored'), (30, 'Pessimistic'), (35, 'Overheated'), (40, 'Worried'), (45, 'Angry'), (50, 'Guilty'), (55, 'Deepens')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thought', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]