
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from articles.views import ArticleViewSet, TagListView, CommentViewSet
from users.views import UserViewSet, UserView, ProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register("users", UserViewSet, basename="users")
router.register("profiles", ProfileViewSet, basename="profiles")
router.register("articles", ArticleViewSet, basename="articles")
article_router = NestedSimpleRouter(router, r"articles", lookup="article")
article_router.register(
    "comments", CommentViewSet, basename="article-comments"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # APIs
    path("api/", include(router.urls)),
    path("api/", include(article_router.urls)),
    path("api/user", UserView.as_view(), name="user"),
    path("api/tags", TagListView.as_view(), name="tags-list"),
    # Frontend
    re_path(r"^(?:.*)$", TemplateView.as_view(template_name="index.html")),
]
