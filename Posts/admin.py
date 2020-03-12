from django.contrib import admin
from Posts.models import Post
from Comments.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    exclude = ['created_date', 'slug', 'likes']


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


# class CommentAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)



# admin.site.register(Post)
