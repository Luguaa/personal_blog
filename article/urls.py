
__author__ = 'Luguaa'
__date__ = '2020/4/30 13:20'

from django.contrib import admin
from django.urls import path
from .views import IndexView, ArticleDetailView, ArticleListView

app_name = 'article'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:article_id>', ArticleDetailView.as_view(), name='article_detail'),
    path('article_list', ArticleListView.as_view(), name='article_list')
]