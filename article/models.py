from datetime import datetime

from django.db import models
from users.models import UserProfile


# Create your models here.
class Tags(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=20, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Channels(models.Model):
    """
    专题
    """
    name = models.CharField(max_length=20, verbose_name='专题')
    subscribed_num = models.IntegerField(default=0, verbose_name='订阅人数')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专题'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=300, verbose_name='摘要')
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    image = models.ImageField(upload_to='articles/%Y/%m', verbose_name='封面图', max_length=100)
    detail = models.TextField(verbose_name='文章详情')
    vote_num = models.IntegerField(default=0, verbose_name='点赞数')
    bookmark_num = models.IntegerField(default=0, verbose_name='收藏数')
    tags = models.ForeignKey(Tags, max_length=20, verbose_name='标签', default='', on_delete=models.SET_DEFAULT)
    channels = models.ForeignKey(Channels, max_length=20, verbose_name='专题', default='', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Video(models.Model):
    """
    视频
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=300, verbose_name='摘要')
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    url = models.CharField(max_length=200, verbose_name='访问地址', default='')
    detail = models.TextField(verbose_name='视频详情')
    vote_num = models.IntegerField(default=0, verbose_name='点赞数')
    bookmark_num = models.IntegerField(default=0, verbose_name='收藏数')
    tags = models.ForeignKey(Tags, max_length=20, verbose_name='标签', default='', on_delete=models.SET_DEFAULT)
    channels = models.ForeignKey(Channels, max_length=20, verbose_name='专题', default='', on_delete=models.SET_DEFAULT)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    """
    首页轮播图
    """
    article = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner", verbose_name="图片", null=True, blank=True)
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title