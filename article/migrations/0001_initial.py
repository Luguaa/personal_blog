# Generated by Django 2.0 on 2020-04-28 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('desc', models.CharField(max_length=300, verbose_name='摘要')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('image', models.ImageField(upload_to='articles/%Y/%m', verbose_name='封面图')),
                ('detail', models.TextField(verbose_name='文章详情')),
                ('vote_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('bookmark_num', models.IntegerField(default=0, verbose_name='收藏数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='专题')),
                ('subscribed_num', models.IntegerField(default=0, verbose_name='订阅人数')),
            ],
            options={
                'verbose_name': '专题',
                'verbose_name_plural': '专题',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('desc', models.CharField(max_length=300, verbose_name='摘要')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('url', models.CharField(default='', max_length=200, verbose_name='访问地址')),
                ('detail', models.TextField(verbose_name='视频详情')),
                ('vote_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('bookmark_num', models.IntegerField(default=0, verbose_name='收藏数')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
    ]
