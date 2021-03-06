# Generated by Django 2.0 on 2020-04-28 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='评论')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('vote_num', models.IntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='数据id')),
                ('fav_type', models.IntegerField(choices=[(1, '文章'), (2, '视频'), (3, '专题')], default=1, verbose_name='收藏类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
    ]
