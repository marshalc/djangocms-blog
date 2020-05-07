from django.urls import path, re_path

from .feeds import FBInstantArticles, LatestEntriesFeed, TagFeed
from .settings import get_setting
from .views import (
    AuthorEntriesView, CategoryEntriesView, PostArchiveView, PostDetailView, PostListView,
    TaggedListView,
)


def get_urls():
    urls = get_setting('PERMALINK_URLS')
    details = []
    for urlconf in urls.values():
        details.append(
            re_path(urlconf, PostDetailView.as_view(), name='post-detail'),
        )
    return details


detail_urls = get_urls()

# module-level app_name attribute as per django 1.9+
app_name = 'djangocms_blog'
urlpatterns = [
    re_path(r'^$', PostListView.as_view(), name='posts-latest'),
    re_path(r'^feed/$', LatestEntriesFeed(), name='posts-latest-feed'),
    re_path(r'^feed/fb/$', FBInstantArticles(), name='posts-latest-feed-fb'),
    re_path(r'^(?P<year>\d{4})/$', PostArchiveView.as_view(), name='posts-archive'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', PostArchiveView.as_view(), name='posts-archive'),
    re_path(r'^author/(?P<username>[\w\.@+-]+)/$', AuthorEntriesView.as_view(), name='posts-author'),
    re_path(r'^category/(?P<category>[\w\.@+-]+)/$', CategoryEntriesView.as_view(), name='posts-category'),
    re_path(r'^tag/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='posts-tagged'),
    re_path(r'^tag/(?P<tag>[-\w]+)/feed/$', TagFeed(), name='posts-tagged-feed'),
] + detail_urls
