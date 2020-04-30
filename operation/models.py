from datetime import datetime

from django.db import models

from article.models import Article
from users.models import UserProfile


# Create your models here.
class ArticleComments(models.Model):
    """文章评论"""
    # TODO:评论用户
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')
    vote_num = models.IntegerField(default=0, verbose_name='点赞数')

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1, "文章"), (2, "视频"), (3, '专题')), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name