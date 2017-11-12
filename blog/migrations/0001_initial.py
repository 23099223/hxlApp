# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='自增id')),
                ('title', models.CharField(max_length=100, verbose_name='博客标题')),
                ('description', models.CharField(max_length=200, verbose_name='博客描述')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('view_count', models.IntegerField(default=100, verbose_name='阅读次数')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('icones', models.ImageField(null=True, upload_to='', verbose_name='插图')),
                ('content', models.TextField(blank=True, null=True, verbose_name='正文')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_name', models.CharField(default='guest', max_length=50, verbose_name='评论人')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('content', models.CharField(max_length=500, verbose_name='评论内容')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='ref1', to='blog.Tags'),
        ),
    ]