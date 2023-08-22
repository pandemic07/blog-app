
from django.urls import path
from . import views

urlpatterns = [
    path('create-blog-post/', views.create_blog_post, name='create-blog-post'),
    path('create-comment/<int:post_id>/', views.create_comment, name='create-comment'),
    path('list-blog-posts/', views.list_blog_posts, name='list-blog-posts'),
    path('list-comments/<int:post_id>/', views.list_comments, name='list-comments'),
    path('update-blog-post/<int:pk>/', views.update_blog_post, name='update-blog-post'),
]
