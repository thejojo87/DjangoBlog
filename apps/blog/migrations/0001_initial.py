# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:34
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章名')),
                ('blog_sn', models.CharField(default='', max_length=50, verbose_name='文章唯一货号')),
                ('click_num', models.IntegerField(default=0, verbose_name='阅读数')),
                ('blog_brief', models.TextField(max_length=500, verbose_name='文章简短描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('blog_main', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo', verbose_name='所属文集')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
            },
        ),
    ]
