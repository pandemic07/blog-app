# blog/admin.py
from django.contrib import admin
from .models import BlogPost,Comment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

# Register the BlogPost model with the custom BlogPostAdmin
admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at', 'updated_at')
    list_filter = ('author',)
    search_fields = ('content',)
    ordering = ('-created_at',)

# Register the Comment model with the customized CommentAdmin
admin.site.register(Comment, CommentAdmin)



