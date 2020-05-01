import markdown
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render
from django.views.generic.base import View

from .models import Article, Channels, Banner, Tags, Video


class IndexView(View):
    """
    文章列表页、首页
    """
    def get(self, request):
        all_articles = Article.objects.all().order_by("-add_time")
        hot_articles = Article.objects.all().order_by("-vote_num")[:5]

        # # 关键词搜索
        # search_keywords = request.GET.get('keywords', '')
        # if search_keywords:
        #     # icontains:类似mysql的like语句，i表示不区分大小写
        #     all_courses = all_courses.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) |
        #                                      Q(detail__icontains=search_keywords))

        # 课程排序
        # 获取排序类型
        # sort = request.GET.get('sort', '')
        # if sort:
        #     if sort == "students":
        #         all_courses = all_courses.order_by('-students')
        #     elif sort == "hot":
        #         all_courses = all_courses.order_by('-click_nums')

        # 对课程进行分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1

        # Provide Paginator with the request object for complete querystring generation
        # 每页显示六个课程
        # p = Paginator(all_articles, 6, request=request)
        #
        # courses = p.page(page)

        return render(request, 'index.html', {
            'all_articles': all_articles,
            # 'sort': sort,
            'hot_articles': hot_articles
        })


class ArticleDetailView(View):
    """
    文章详情页
    """
    def get(self, request, article_id):
        # 获取课程id
        article = Article.objects.get(id=int(article_id))


        # # 用户认证
        # if request.user.is_authenticated():
        #     # 收藏课程
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course_id, fav_type=1):
        #         has_fav_course = True
        #
        #     # 收藏机构
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        # 相关课程推荐
        # tag = course.tag
        # if tag:
        #     # 获取相同tag的课程
        #     relate_courses = Course.objects.filter(tag=tag)[:1]
        # else:
        #     relate_courses = []

        return render(request, 'post.html', {
            'article': article,
        })


class ArticleListView(View):
    """
    文章列表页、首页
    """
    def get(self, request):
        all_articles = Article.objects.all().order_by("-add_time")
        hot_articles = Article.objects.all().order_by("-vote_num")[:5]

        # # 关键词搜索
        # search_keywords = request.GET.get('keywords', '')
        # if search_keywords:
        #     # icontains:类似mysql的like语句，i表示不区分大小写
        #     all_courses = all_courses.filter(Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) |
        #                                      Q(detail__icontains=search_keywords))

        # 课程排序
        # 获取排序类型
        # sort = request.GET.get('sort', '')
        # if sort:
        #     if sort == "students":
        #         all_courses = all_courses.order_by('-students')
        #     elif sort == "hot":
        #         all_courses = all_courses.order_by('-click_nums')

        # 对课程进行分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1

        # Provide Paginator with the request object for complete querystring generation
        # 每页显示六个课程
        # p = Paginator(all_articles, 6, request=request)
        #
        # courses = p.page(page)

        return render(request, 'article_list.html', {
            'all_articles': all_articles,
            # 'sort': sort,
            'hot_articles': hot_articles
        })

