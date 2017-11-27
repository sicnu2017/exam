# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 21:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MchoiceProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128, verbose_name='题目')),
                ('optionA', models.CharField(blank=True, max_length=64, verbose_name='选项A')),
                ('optionB', models.CharField(blank=True, max_length=64, verbose_name='选项B')),
                ('optionC', models.CharField(blank=True, max_length=64, verbose_name='选项C')),
                ('optionD', models.CharField(blank=True, max_length=64, verbose_name='选项D')),
                ('optionE', models.CharField(blank=True, max_length=64, verbose_name='选项E')),
                ('answer', models.CharField(blank=True, max_length=12, verbose_name='正确答案')),
                ('level', models.CharField(choices=[('simple', '简单'), ('medium', '中等'), ('hard', '困难')], default='simple', max_length=12, verbose_name='难易度')),
                ('value', models.DecimalField(blank=True, decimal_places=1, max_digits=2, verbose_name='分值')),
                ('is_multiple', models.BooleanField(default=False, verbose_name='是否多选')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='增加时间')),
                ('createuser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '选择题',
                'verbose_name_plural': '选择题',
                'db_table': 'MchoiceProfile',
            },
        ),
    ]
