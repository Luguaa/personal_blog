from django.contrib import admin
from .models import Article, Channels, Banner, Tags, Video


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'detail', 'author', 'add_time', 'image', 'vote_num', 'bookmark_num', 'tags', 'channels']


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'subscribed_num']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['article', 'image', 'index', 'add_time']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'detail', 'author', 'add_time', 'url', 'vote_num', 'bookmark_num', 'tags', 'channels']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Channels, ChannelAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(Video, VideoAdmin)

