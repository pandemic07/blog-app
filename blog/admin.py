from django.contrib import admin
from .models import BlogPost,Comment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at', 'updated_at')
    list_filter = ('author',)
    search_fields = ('content',)
    ordering = ('-created_at',)

admin.site.register(Comment, CommentAdmin)



