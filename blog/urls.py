from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TagPostListView,
    SearchPostListView,
    CategoryPostListView,
    CommentCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('tags/<slug:tag_slug>/', TagPostListView.as_view(), name='post_by_tag'),
    path('search/', SearchPostListView.as_view(), name='search'),
]
